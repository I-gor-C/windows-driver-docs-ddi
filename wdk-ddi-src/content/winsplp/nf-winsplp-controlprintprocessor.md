---
UID: NF.winsplp.ControlPrintProcessor
title: ControlPrintProcessor
author: windows-driver-content
description: A print processor's ControlPrintProcessor function allows the spooler to control a print job.
old-location: print\controlprintprocessor.htm
old-project: print
ms.assetid: a0a19747-ab39-4606-a49b-78e5e056da32
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: ControlPrintProcessor
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winsplp.h
req.include-header: Winsplp.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ControlPrintProcessor
req.alt-loc: Nwprint.lib,Nwprint.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Nwprint.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# ControlPrintProcessor function



## -description
<p>A print processor's <b>ControlPrintProcessor</b> function allows the spooler to control a print job.</p>


## -syntax

````
BOOL ControlPrintProcessor(
  _In_ HANDLE hPrintProcessor,
  _In_ DWORD  Command
);
````


## -parameters
<dl>

### -param <i>hPrintProcessor</i> [in]

<dd>
<p>Caller-supplied print processor handle. This is the handle returned by a previous call to <a href="..\winsplp\nf-winsplp-openprintprocessor.md">OpenPrintProcessor</a>.</p>
</dd>

### -param <i>Command</i> [in]

<dd>
<p>Caller-supplied command indicating the type of operation to perform. The following commands are valid:</p>
<table>
<tr>
<th>Command</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>JOB_CONTROL_CANCEL</p>
</td>
<td>
<p>The function should cancel the current print job.</p>
</td>
</tr>
<tr>
<td>
<p>JOB_CONTROL_PAUSE</p>
</td>
<td>
<p>The function should pause the current print job.</p>
</td>
</tr>
<tr>
<td>
<p>JOB_CONTROL_RESUME</p>
</td>
<td>
<p>The function should resume the current print job.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function should return <b>TRUE</b>. If the operation fails, the function should call SetLastError to set an error code, and then return <b>FALSE</b>.</p>

## -remarks
<p>Print processors are required to export a <b>ControlPrintProcessor</b> function. The spooler calls the function when an application calls the SetJob function, described in the Microsoft Windows SDK documentation.</p>

<p>Based on the value received for <i>Command</i>, the function should either pause, resume, or cancel the current job. The <b>ControlPrintProcessor</b> function can be called asynchronously while the print processor's <a href="..\winsplp\nf-winsplp-printdocumentonprintprocessor.md">PrintDocumentOnPrintProcessor</a> function is executing. Thus some sort of synchronization technique must be employed, such as setting an internally-defined event object to pause a job and resetting the event object when the job is resumed. The <b>ControlPrintProcessor</b> function can quickly return after setting or resetting the event object, and PrintDocumentOnPrintProcessor can wait for the event to be in the proper state.</p>

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
<dt>Winsplp.h (include Winsplp.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Nwprint.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\winsplp\nf-winsplp-openprintprocessor.md">OpenPrintProcessor</a>
</dt>
<dt>
<a href="..\winsplp\nf-winsplp-printdocumentonprintprocessor.md">PrintDocumentOnPrintProcessor</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20ControlPrintProcessor function%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
