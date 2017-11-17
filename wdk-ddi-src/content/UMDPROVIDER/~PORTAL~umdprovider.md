# Declarations in the umdprovider header
This header Umdprovider contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [EnableCallback function](nf-umdprovider-enablecallback.md) | TBD |
| [UMDEtwLogMapAllocation function](nf-umdprovider-umdetwlogmapallocation.md) | Describes how a Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) memory allocation, or a portion of the allocation, is being used. |
| [UMDEtwLogMapAllocation function](nf-umdprovider-umdetwlogmapallocation~r1.md) | Describes how a Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) memory allocation, or a portion of the allocation, is being used. |
| [UMDEtwRegister function](nf-umdprovider-umdetwregister.md) | Registers the event trace provider. The driver should call this function before it makes any calls to log events. |
| [UMDEtwRegister function](nf-umdprovider-umdetwregister~r1.md) | Registers the event trace provider. The driver should call this function before it makes any calls to log events. |
| [UMDEtwUnregister function](nf-umdprovider-umdetwunregister.md) | Unregisters the event trace provider. Call this function before the user-mode driver is unloaded. After this function is called, the driver should not make any other calls to log events. |
| [UMDEtwLogUnmapAllocation function](nf-umdprovider-umdetwlogunmapallocation~r1.md) | Indicates that a Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) memory allocation, or a portion of the allocation, is no longer being used. Call this function whether or not the allocation is being destroyed. |
| [LogMapAllocation function](nf-umdprovider-logmapallocation.md) | TBD |
| [UMDEtwUnregister function](nf-umdprovider-umdetwunregister~r1.md) | Unregisters the event trace provider. Call this function before the user-mode driver is unloaded. After this function is called, the driver should not make any other calls to log events. |
| [UMDEtwLogUnmapAllocation function](nf-umdprovider-umdetwlogunmapallocation.md) | Indicates that a Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) memory allocation, or a portion of the allocation, is no longer being used. Call this function whether or not the allocation is being destroyed. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFNUMDETW_RUNDOWN callback function](nc-umdprovider-pfnumdetw-rundown.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UMDETW_ALLOCATION_USAGE structure](ns-umdprovider--umdetw-allocation-usage.md) | Indicates the reason for mapping from a Microsoft Direct3D memory allocation to a Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) allocation. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [UMDETW_ALLOCATION_SEMANTIC enumeration](ne-umdprovider--umdetw-allocation-semantic.md) | Indicates what a memory allocation is used for if the allocation is internal to the user-mode driver. |

This header is used in these topics:

- [display](..content/_display)
