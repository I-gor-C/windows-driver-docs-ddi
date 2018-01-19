---
UID : NF:ntifs.FsRtlSetupAdvancedHeader
title : FsRtlSetupAdvancedHeader function
author : windows-driver-content
description : The FsRtlSetupAdvancedHeader macro is used by file systems to initialize an FSRTL_ADVANCED_FCB_HEADER structure for use with filter contexts.
old-location : ifsk\fsrtlsetupadvancedheader.htm
old-project : ifsk
ms.assetid : 8bcf7bbf-6c41-4683-9a62-d408b120c7b9
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : FsRtlSetupAdvancedHeader
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntifs.h
req.include-header : Ntifs.h, Fltkernel.h
req.target-type : Desktop
req.target-min-winverclnt : Available on Microsoft Windows XP and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : FsRtlSetupAdvancedHeader
req.alt-loc : ntifs.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : <= APC_LEVEL
req.typenames : TOKEN_TYPE
---


# FsRtlSetupAdvancedHeader function
The <b>FsRtlSetupAdvancedHeader</b> macro is used by file systems to initialize an <a href="..\ntifs\ns-ntifs-_fsrtl_advanced_fcb_header.md">FSRTL_ADVANCED_FCB_HEADER</a> structure for use with filter contexts.

## Syntax

````
VOID FsRtlSetupAdvancedHeader(
  _In_ PVOID       AdvancedHeader,
  _In_ PFAST_MUTEX FastMutex
);
````

## Parameters

`AdvHdr`



`FMutex`




## Return Value

None

## Remarks

File systems use the <b>FsRtlSetupAdvancedHeader</b> macro to initialize an <a href="..\ntifs\ns-ntifs-_fsrtl_advanced_fcb_header.md">FSRTL_ADVANCED_FCB_HEADER</a> structure for use with filter contexts. 

When the advanced FCB header structure is no longer required, the file system must call <a href="..\ntifs\nf-ntifs-fsrtlteardownperstreamcontexts.md">FsRtlTeardownPerStreamContexts</a> to free all associated per-stream context structures. 

For more information, see <a href="https://msdn.microsoft.com/d908ee30-a433-460c-8c14-883702b4f810">Tracking Per-Stream Context in a Legacy File System Filter Driver</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h, Fltkernel.h) |
| **Library** |  |
| **IRQL** | <= APC_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\ntifs\ns-ntifs-_fsrtl_advanced_fcb_header.md">FSRTL_ADVANCED_FCB_HEADER</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs-_fsrtl_per_stream_context.md">FSRTL_PER_STREAM_CONTEXT</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlgetperstreamcontextpointer.md">FsRtlGetPerStreamContextPointer</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlinitperstreamcontext.md">FsRtlInitPerStreamContext</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlinsertperstreamcontext.md">FsRtlInsertPerStreamContext</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtllookupperstreamcontext.md">FsRtlLookupPerStreamContext</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlremoveperstreamcontext.md">FsRtlRemovePerStreamContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547285">FsRtlSupportsPerStreamContexts</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlteardownperstreamcontexts.md">FsRtlTeardownPerStreamContexts</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlSetupAdvancedHeader function%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>