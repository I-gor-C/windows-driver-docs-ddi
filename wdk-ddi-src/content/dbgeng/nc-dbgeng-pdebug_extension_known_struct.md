---
UID : NC:dbgeng.PDEBUG_EXTENSION_KNOWN_STRUCT
title : PDEBUG_EXTENSION_KNOWN_STRUCT
author : windows-driver-content
description : The engine calls the KnownStructOutput callback function to request information about structures that the extension DLL can format for printing. The engine calls this function for the following reasons.
old-location : debugger\knownstructoutput.htm
old-project : debugger
ms.assetid : 76b7e097-4953-4988-8999-07bbfbd65912
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _DOT4_ACTIVITY, *PDOT4_ACTIVITY, DOT4_ACTIVITY
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : dbgeng.h
req.include-header : 
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KnownStructOutput
req.alt-loc : dbgeng.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---


# PDEBUG_EXTENSION_KNOWN_STRUCT callback function
The engine calls the <i>KnownStructOutput</i> callback function to request information about structures that the extension DLL can format for printing. The engine calls this function for the following reasons.

## Syntax

```
PDEBUG_EXTENSION_KNOWN_STRUCT PdebugExtensionKnownStruct;

HRESULT PdebugExtensionKnownStruct(
  ULONG Flags,
  ULONG64 Offset,
  PSTR TypeName,
  PSTR Buffer,
  PULONG BufferChars
)
{...}
```

## Parameters

`Flags`



`Offset`



`TypeName`



`Buffer`

<b>When getting a list of names:</b>  Receives a list of the names of the structures that the extension can format for printing.  One null character must appear between each pair of names.  The list must be terminated with two null characters. The number of characters written to this buffer must not exceed the value of <i>BufferSize</i>.

<b>When asking whether a name should be printed:</b> Unused.

<b>When getting a single-line representation:</b>  Receives a representation  of the structure, identified by <i>StructName</i> and <i>Address</i>, as a string. The number of characters written to this buffer must not exceed the value of <i>BufferSize</i>.

`BufferChars`




## Return Value

<dl>
<dt><b>S_OK</b></dt>
</dl><b>When getting a list of names:</b><i> Buffer</i> contains the requested list of names.

<b>When asking whether a name should be printed:</b>  The printing of the name should be suppressed. That is, the name should not be printed.   

<b>When getting a single-line representation:</b><i> Buffer</i> contains the requested single-line representation.
<dl>
<dt><b>S_FALSE</b></dt>
</dl><b>When getting a list of names:</b><i> BufferSize</i> was too small on input. On output, <i> BufferSize</i> contains the required buffer size.

<b>When asking whether a name should be printed:</b>  The printing of the name should not be suppressed. That is, the name should be printed.   

<b>When getting a single-line representation:</b><i> BufferSize</i> was too small on input. On output, <i> BufferSize</i> contains the required buffer size.

 

All other return values indicate that the function failed.  The engine will continue ignoring the contents of <i>Buffer</i>.

## Remarks

This function is optional.  An extension DLL only needs to export <b>KnownStructOutput</b> if it has the ability to format special structures for printing on a single line.  The engine looks for this function by name in the extension DLL.

After initializing the extension DLL, the engine calls this function to query the DLL for the list of structure names it knows how to print.  Then, whenever the engine prints a summary of one of the structures whose name is in the list, it calls this function to format the structure for printing.


<a href="..\dbgeng\nc-dbgeng-pdebug_stack_provider_freestacksymframes.md">KnownStructOutput</a> is called <b>PDEBUG_EXTENSION_KNOWN_STRUCT</b>   in the Dbgeng.h header file.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\dbgeng\nc-dbgeng-pdebug_extension_initialize.md">DebugExtensionInitialize</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20PDEBUG_EXTENSION_KNOWN_STRUCT callback function%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>