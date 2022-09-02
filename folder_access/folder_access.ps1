# Сброс значения переменных. для чистоты эксперимента.
$SelectedGroup=0
$Index=0
$Groups=0
$Group=0
$AddAccess=0
$Access=0
$OwnerName=0
$FullName=0
$UserName=0
$SaName=0


Function FindGroups { 
# Передаем в переменную логин пользователя запустившего скрипт
$OwnerName = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name.replace("*****\","")

# получаем параметр "DistinguishedName" для дальнейшего поиска групп по параметру "ManagedBy"
$Global:FullName = Get-ADUser $OwnerName | ForEach-Object -Process {$_.DistinguishedName}

# Получаем список групп доступа к папкам на диске * (по маске "\\***.local\files\Project\*" ) В $_.Description , в которых пользователь запустивший скрипт является владельцем (ManagedBy)/ 
# $Groups будет содержать(коллекцию) все группы удовлетворяющие фильтру
$Global:Groups = Get-ADPrincipalGroupMembership $OwnerName | Get-ADGroup -Properties managedby, Description, Name | 
    Where-Object {$_.Description -like "\\***.local\files\Project\*"-and $_.Name -like "*RW" -and $_.ManagedBy -like "$Global:FullName"} 
    }

Function ChekCount {     # Функция. Запрос номера элемента из списка. Проверка
 Try   # Ловим исключение если пользователь ввел "...какую то дичь"© вместо Int32 и ругаемся! И снова запускаем функцию.
 {      
    [int]$SelectedGroup =  Read-Host "Выберите каталог (Номер из списка)" 
    $Global:Index = $SelectedGroup -=1 # т.к. для удобства пользователя мы показываем нумерацию начиная с 1, а индекс коллекции начинается с 0, то тут мы делаем -1.
    if ($Global:Index -lt $Groups.Count -and $Global:Index -ge 0){ }  # Проверяем что пользователь ввел число меньше либо равно кол-ву элементов в коллеции и больше 0.
 Else
 {
    Write-Host "Пожалуйста, выберите корректный номер из списка" -BackgroundColor White -ForegroundColor Red; ChekCount
    }
}
 catch [System.Management.Automation.RuntimeException] # Ловим исключение. Если Юзер ввел не число
 {Write-host "Пожалуйста, выберите корректный номер из списка" -BackgroundColor White -ForegroundColor Red; ChekCount} # Вот тут ругаемся и снова запускаем функцию.
  }

Function LoadMembers {
Write-Host "Следующие пользователи имеют доступ на чтение" -BackgroundColor Black -ForegroundColor Green 
 Get-ADGroupMember $Global:Groups[$Global:Index].name.Replace("RW","RO") | Get-ADUser  | select name, SamAccountName | format-table SamAccountName, name -AutoSize
  Write-Host "Следующие пользователи имеют доступ на чтение и запись" -BackgroundColor Black -ForegroundColor Green 
   Get-ADGroupMember $Global:Groups[$Global:Index].name | Get-ADUser  | select name, SamAccountName | format-table SamAccountName, name -AutoSize   

}

Function AddAccess {   # Запрашиваем уровень доступа - RO\RW
    
    Write-Host "Какой Уровень Доступа Необходимо Предоставить?" -BackgroundColor Black -ForegroundColor Green 
        Write-Host "1. Только чтение"
    Write-Host "2. Чтение и Запись"
    $AddAccess = Read-Host "Выберите значение из списка"  
    
        Switch ("$AddAccess") {
         1 {$Global:Access = "RO"}
         2 {$Global:Access = "RW"}
         default {Write-Host "Пожалуйста, введите 1 или 2 !!!" -BackgroundColor Black -ForegroundColor Red; AddAccess}
         }
   FindUser
    Add-AdGroupMember -Identity $Global:Groups[$Global:Index].name.Replace("RW","$Global:access") -Members $Global:SaName.SamAccountName 
      ChekAdAccess
        }

Function ChekAdAccess {
$TempGroupInfo = $Groups[$Index].name.Replace("RW","$access")
$CheckGroup = Get-ADGroup "$TempGroupInfo"
if  ( Get-ADUser $Global:SaName.SamAccountName -Properties MemberOf | Where-Object {$_.MemberOf -like $Global:CheckGroup.DistinguishedName} ) #DistinguishedName
{
    Write-host "Доступ предоставлен" -ForegroundColor Black -BackgroundColor Green
}
Else
{
      Write-Host "Произошла ошибка. Доступ не предоставлен. Обратитесь в отдел поддержки пользователей" -BackgroundColor White -ForegroundColor Red
}

Pause
Break
}

Function RemoveAccess {   # Запрашиваем уровень доступа - RO\RW
    
    Write-Host "Какой уровень доступа необходимо отозвать?" -BackgroundColor Black -ForegroundColor Green 
    Write-Host "1. Отозвать доступ на запись(В этом случае, вероятно, потребуется предоставить доступ на чтение)"
    Write-Host "2. Отозвать доступ полностью"
    $AddAccess = Read-Host "Выберите значение из списка"  
    
        Switch ("$AddAccess") {
         1 {FindUser
              Remove-AdGroupMember -Identity $Global:Groups[$Global:Index].name -Members $Global:SaName.SamAccountName}
         2 {FindUser
              Remove-AdGroupMember -Identity $Global:Groups[$Global:Index].name.Replace("RW","RO") -Members $Global:SaName.SamAccountName
               Remove-AdGroupMember -Identity $Global:Groups[$Global:Index].name -Members $Global:SaName.SamAccountName}
         
         default {Write-Host "Пожалуйста, введите 1 или 2 !!!" -BackgroundColor Black -ForegroundColor Red; AddAccess}
         }
          }

Function FindUser {   #Просим ввести логин. затем "ВЖУХ!!!!" 

try {  # Ловим исключение. если указанный юзер не найден в АД. Если все гуд, выполняем код ниже. Если не все гуд, то catch
      Write-Host "Введите логин пользователя (прим.: Sivanov )" -BackgroundColor Black -ForegroundColor Green
      $Global:UserName = Read-Host
      $Global:SaName = Get-ADUser $UserName -Properties SamAccountName, DisplayName |Where-Object {$_.SamAccountName -EQ "$UserName"}
      Write-Output $SaName.DisplayName
      ChekUser
}
catch [Microsoft.ActiveDirectory.Management.ADIdentityNotFoundException] 
{
      Write-host  "Пользователь не найден в домене! Пожалуйста проверьте логин" -ForegroundColor White -BackgroundColor Red; FindUser # Вот тут ругаемся и снова запускаем функцию.
          }

}

Function ChekUser {
Write-Host -BackgroundColor Black -ForegroundColor Green "Проверьте ФИО и табельный номер сотрудника, перед тем как предоставить доступ
Выбран корректный сотрудник? 
Введите Да или нет"

      $QA = Read-Host
        
        switch ($QA) {
        Да  {continue}
        Нет {Write-Host -BackgroundColor Black -ForegroundColor Green "Давайте заново поищем сотрудника"
                FindUser   
        }
        Default {Write-Host "Пожалуйста, введите Значение Да или Нет!!!" -BackgroundColor Black -ForegroundColor Red;  ChekUser}
        }



}

Function LoadMembers {
Write-Host "Следующие пользователи имеют доступ на чтение" -BackgroundColor Black -ForegroundColor Green 
 Get-ADGroupMember $Global:Groups[$Global:Index].name.Replace("RW","RO") | Get-ADUser  | select name, SamAccountName | format-table SamAccountName, name -AutoSize
  Write-Host "Следующие пользователи имеют доступ на чтение и запись" -BackgroundColor Black -ForegroundColor Green 
   Get-ADGroupMember $Global:Groups[$Global:Index].name | Get-ADUser  | select name, SamAccountName | format-table SamAccountName, name -AutoSize   

}

Function SelectAction {

Write-host "Выберите действие, которое необходимо выполнить" -ForegroundColor Black -BackgroundColor Green 
Write-host "1. Показать всех пользователей, которые имеют доступ к папке. 
2. Отозвать доступ у пользователя.
3. Предоставить доступ пользователю." 

$Action =  Read-Host "Выберите действие, которое необходимо выполнить"
Switch ("$Action") {
         1 {LoadMembers; Write-host "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - "# выполняем функцию и Украшательства   #Выгружаем список членов группы - SamAccountName, name
            pause
            break
                 }
         2 {RemoveAccess; Write-host "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - "# выполняем функцию и Украшательства
            pause
            break
                 }
         3 {AddAccess; Write-host "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - "# выполняем функцию и Украшательства
            FindUser
            pause
            break
                 }
         default {Write-Host "Пожалуйста, введите Значение 1-3!!!" -BackgroundColor Black -ForegroundColor Red;  SelectAction}
         }
   }


FindGroups

If ($Groups -ne $Null) {}  # Если папки нашли - ну ок, продолжаем. Если не нашли папки, говорим сообщение из Else
Else
   { 
    Write-Host "Папки не найдены!!! Произошла ошибка или вы не являетесь влдельцем ни одно каталога." -BackgroundColor White -ForegroundColor Red
    pause
    Break
        }

Write-host "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - "    # Украшательства     
Write-host "Вы являетесь владельцем следующих каталогов на диске * " -ForegroundColor Black -BackgroundColor Green 
 

$i = 0  # Переменная i=индекс элемента в коллекции
   foreach ($Group in $Groups) #Дергаем значения из коллекции
{
    $i++ # Добавляем +1 к индексу, чтоб юзер видел нумерацию начиная с единицы
     Write-host "$i. " -NoNewline
     Write-host $Group.Description.replace("\\***.local\files\Project\","")
    }

ChekCount ; Write-host "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - "# выполняем функцию и Украшательства 

SelectAction


