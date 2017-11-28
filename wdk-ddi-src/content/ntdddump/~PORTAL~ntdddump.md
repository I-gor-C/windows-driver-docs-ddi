# Ntdddump.h header


This header is used by unknown technology.

Ntdddump.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [DUMP_FINISH callback](nc-ntdddump-dump-finish.md) | The Dump_Finish callback routine is called after writing all the dump data. The dump port driver generally flushes the cache to ensure the data is stored on the storage media before the system powers down. |
| [DUMP_READ callback](nc-ntdddump-dump-read.md) | The Dump_Read callback routine is called after the read from the dump port driver. The filter driver can access the dump data during the call to this routine. |
| [DUMP_START callback](nc-ntdddump-dump-start.md) | The Dump_Start callback routine is called after initializing the dump driver and just before starting the dump write process. |
| [DUMP_UNLOAD callback](nc-ntdddump-dump-unload.md) | The Dump_Unload callback routine is called when the dump stack is unloaded. |
| [DUMP_WRITE callback](nc-ntdddump-dump-write.md) | The Dump_Write callback routine is called before the write to the dump port driver. The filter driver can access the dump data at this time. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [FILTER_EXTENSION structure](ns-ntdddump--filter-extension.md) | The crash dump driver passes a pointer to a FILTER_EXTENSION structure when the filter driver callback routines are called. |
| [FILTER_INITIALIZATION_DATA structure](ns-ntdddump--filter-initialization-data.md) | The filter driver fills in a FILTER_INITIALIZATION_DATA structure and returns it to the crash dump driver. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [FILTER_DUMP_TYPE enumeration](ne-ntdddump--filter-dump-type.md) | The FILTER_DUMP_TYPE enumeration indicates the type of dump stack that this instance of the filter driver is loaded on. |
