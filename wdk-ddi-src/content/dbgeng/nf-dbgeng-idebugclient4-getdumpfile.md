---
UID: NF:dbgeng.IDebugClient4.GetDumpFile
title: IDebugClient4::GetDumpFile method
author: windows-driver-content
description: The GetDumpFile method describes the files containing supporting information that were used when opening the current dump target.
old-location: debugger\getdumpfile.htm
old-project: debugger
ms.assetid: 06317b65-4853-40da-9131-9983918b7157
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: GetDumpFile method [Windows Debugging], GetDumpFile method [Windows Debugging], IDebugClient4 interface, GetDumpFile method [Windows Debugging], IDebugClient5 interface, GetDumpFile,IDebugClient4.GetDumpFile, IDebugClient4, IDebugClient4 interface [Windows Debugging], GetDumpFile method, IDebugClient4::GetDumpFile, IDebugClient5 interface [Windows Debugging], GetDumpFile method, IDebugClient5::GetDumpFile, IDebugClient_f4f1540c-116c-4e74-ad19-10beb0ac2739.xml, dbgeng/IDebugClient4::GetDumpFile, dbgeng/IDebugClient5::GetDumpFile, debugger.getdumpfile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	dbgeng.h
api_name:
-	IDebugClient4.GetDumpFile
-	IDebugClient5.GetDumpFile
product:
- Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---


# IDebugClient4::GetDumpFile method
The <b>GetDumpFile</b>  method describes the files containing supporting information that were used when opening the current dump target.

## Syntax

```
HRESULT GetDumpFile(
  ULONG    Index,
  PSTR     Buffer,
  ULONG    BufferSize,
  PULONG   NameSize,
  PULONG64 Handle,
  PULONG   Type
);
```

## Parameters

`Index`

Specifies which file to describe.  <i>Index</i> can take values between zero and the number of files minus one; the number of files can be found by using <a href="https://msdn.microsoft.com/library/windows/hardware/ff547887">GetNumberDumpFiles</a>.

`Buffer`

Receives the file name.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.

`BufferSize`

Specifies the size in characters of the buffer <i>Buffer</i>.

`NameSize`

Receives the size of the file name.  If <i>NameSize</i> is <b>NULL</b>, this information is not returned.

`Handle`

Receives the file handle of the file.  If <i>Handle</i> is <b>NULL</b>, this information is not returned.

`Type`

Receives the type of the file.


## Return Value

This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>S_OK</b></dt>
</dl>
</td>
<td width="60%">
The method was successful.

</td>
</tr>
</table>

## Remarks

For more information about crash dump files, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542783">Dump-File Targets</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537865">AddDumpInformationFile</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff537874">AddDumpInformationFileWide</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547887">GetNumberDumpFiles</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550494">IDebugClient4</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550497">IDebugClient5</a>