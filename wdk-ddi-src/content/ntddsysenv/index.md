---
UID : NA:ntddsysenv
ms.assetid : 8081c1fb-7fac-3c8c-b9a7-bcc62bf38982
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# ntddsysenv.h header



ntddsysenv.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_SYSENV_ENUM_VARIABLES](ni-ntddsysenv-ioctl_sysenv_enum_variables.md) | Returns information about system environment variables using SysEnv device. |
| [IOCTL_SYSENV_GET_VARIABLE](ni-ntddsysenv-ioctl_sysenv_get_variable.md) | Gets the value of the specified system environment variables using SysEnv device. |
| [IOCTL_SYSENV_QUERY_VARIABLE_INFO](ni-ntddsysenv-ioctl_sysenv_query_variable_info.md) | Returns information about system environment variables using SysEnv device. |
| [IOCTL_SYSENV_SET_VARIABLE](ni-ntddsysenv-ioctl_sysenv_set_variable.md) | Sets the value of the specified system environment variables using SysEnv device. |




## Structures
| Title | Description |
| ---- |:---- |
| [_SYSENV_VALUE](ns-ntddsysenv-_sysenv_value.md) | Stores the value of a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_GET_VARIABLE request. |
| [_SYSENV_VARIABLE](ns-ntddsysenv-_sysenv_variable.md) | Stores the name a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_GET_VARIABLE request. |
| [_SYSENV_VARIABLE_INFO](ns-ntddsysenv-_sysenv_variable_info.md) | Stores the information about a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_QUERY_VARIABLE_INFO request. |
| [_XVARIABLE_NAME](ns-ntddsysenv-_xvariable_name.md) | Stores the name of a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_ENUM_VARIABLES request. |
| [_XVARIABLE_NAME_AND_VALUE](ns-ntddsysenv-_xvariable_name_and_value.md) | Stores the name and value of a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_ENUM_VARIABLES and IOCTL_SYSENV_SET_VARIABLE requests. |