# Ntddsysenv.h header


This header is used by unknown technology.

Ntddsysenv.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [SYSENV_VALUE structure](ns-ntddsysenv--sysenv-value.md) | Stores the value of a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_GET_VARIABLE request. |
| [SYSENV_VARIABLE structure](ns-ntddsysenv--sysenv-variable.md) | Stores the name a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_GET_VARIABLE request. |
| [SYSENV_VARIABLE_INFO structure](ns-ntddsysenv--sysenv-variable-info.md) | Stores the information about a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_QUERY_VARIABLE_INFO request. |
| [XVARIABLE_NAME structure](ns-ntddsysenv--xvariable-name.md) | Stores the name of a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_ENUM_VARIABLES request. |
| [XVARIABLE_NAME_AND_VALUE structure](ns-ntddsysenv--xvariable-name-and-value.md) | Stores the name and value of a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_ENUM_VARIABLES and IOCTL_SYSENV_SET_VARIABLE requests. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_SYSENV_ENUM_VARIABLES IOCTL](ni-ntddsysenv-ioctl-sysenv-enum-variables.md) | Returns information about system environment variables using SysEnv device. |
| [IOCTL_SYSENV_GET_VARIABLE IOCTL](ni-ntddsysenv-ioctl-sysenv-get-variable.md) | Gets the value of the specified system environment variables using SysEnv device. |
| [IOCTL_SYSENV_QUERY_VARIABLE_INFO IOCTL](ni-ntddsysenv-ioctl-sysenv-query-variable-info.md) | Returns information about system environment variables using SysEnv device. |
| [IOCTL_SYSENV_SET_VARIABLE IOCTL](ni-ntddsysenv-ioctl-sysenv-set-variable.md) | Sets the value of the specified system environment variables using SysEnv device. |
