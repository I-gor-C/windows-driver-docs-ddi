---
UID: NF.dbgeng.IDebugClient4.GetNumberDumpFiles
title: IDebugClient4::GetNumberDumpFiles
author: windows-driver-content
description: The GetNumberDumpFiles method returns the number of files containing supporting information that were used when opening the current dump target.
old-location: debugger\getnumberdumpfiles.htm
old-project: debugger
ms.assetid: d3fa4314-2f11-4ac4-86bd-3eb3f3ea9029
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugClient4, GetNumberDumpFiles, IDebugClient4::GetNumberDumpFiles
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugClient4.GetNumberDumpFiles,IDebugClient5.GetNumberDumpFiles
req.alt-loc: dbgeng.h
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
req.iface: IDebugClient4
---

# IDebugClient4::GetNumberDumpFiles method



## -description
<p>The <b>GetNumberDumpFiles</b> method returns the number of files containing supporting information that were used when opening the current dump target.</p>


## -syntax

````
HRESULT GetNumberDumpFiles(
  [out] PULONG Number
);
````


## -parameters
<dl>

### -param <i>Number</i> [out]

<dd>
<p>Receives the number of files.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>For more information about crash dump files, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542783">Dump-File Targets</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient4.md">IDebugClient4</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>
</dt>
<dt>
<a href="debugger.getdumpfile">GetDumpFile</a>
</dt>
<dt>
<a href="debugger.adddumpinformationfile">AddDumpInformationFile</a>
</dt>
<dt>
<a href="debugger.adddumpinformationfilewide">AddDumpInformationFileWide</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient4::GetNumberDumpFiles method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
