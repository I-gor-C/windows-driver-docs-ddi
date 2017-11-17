# Declarations in the ntdddump header
This header Ntdddump contains these programming interfaces:

Enum

| Title        | Description    |
| ------------- |:-------------:|
| [FILTER_CALLBACK enumeration](ne-ntdddump--filter-callback.md) | TBD |
| [FILTER_DUMP_TYPE enumeration](ne-ntdddump--filter-dump-type.md) | The FILTER_DUMP_TYPE enumeration indicates the type of dump stack that this instance of the filter driver is loaded on. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [FILTER_INITIALIZATION_DATA structure](ns-ntdddump--filter-initialization-data.md) | The filter driver fills in a FILTER_INITIALIZATION_DATA structure and returns it to the crash dump driver. |
| [FILTER_EXTENSION structure](ns-ntdddump--filter-extension.md) | The crash dump driver passes a pointer to a FILTER_EXTENSION structure when the filter driver callback routines are called. |

This header is used in these topics:

- [Storage](..content/_Storage)
