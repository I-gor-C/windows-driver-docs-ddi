---
UID: NF.winsplp.WritePort
title: WritePort
author: windows-driver-content
description: A port monitor's WritePort function writes data to a printer port.
old-location: print\writeport.htm
old-project: print
ms.assetid: 31229c78-0bea-44eb-9f1a-d1bce8a16a3e
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: WritePort
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
req.alt-api: WritePort
req.alt-loc: winsplp.h
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
req.iface: 
req.product: Windows 10 or later.
---

# WritePort function



## -description
<p>A port monitor's <code>WritePort</code> function writes data to a printer port.</p>


## -syntax

````
BOOL WritePort(
  _In_  HANDLE  hPort,
  _In_  LPBYTE  pBuffer,
        DWORD   cbBuf,
  _Out_ LPDWORD pcbWritten
);
````


## -parameters
<dl>

### -param <i>hPort</i> [in]

<dd>
<p>Caller-supplied port handle.</p>
</dd>

### -param <i>pBuffer</i> [in]

<dd>
<p>Caller-supplied pointer to a buffer containing data to be written to the port.</p>
</dd>

### -param <i>cbBuf</i> 

<dd>
<p>Caller-supplied size, in bytes, of <i>pBuffer</i>.</p>
</dd>

### -param <i>pcbWritten</i> [out]

<dd>
<p>Caller-supplied pointer to a location to receive the number of bytes successfully written to the port.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function should return <b>TRUE</b>. Otherwise it should return <b>FALSE</b>.</p>

## -remarks
<p>
<a href="NULL">Language monitors</a> and port monitor server DLLs are required to define a <code>WritePort</code> function and include the function's address in a <a href="..\winsplp\ns-winsplp--monitor2.md">MONITOR2</a> structure.</p>

<p>The handle received as the function's <i>hPort</i> argument is the port handle that the monitor's <a href="..\winsplp\nf-winsplp-openport.md">OpenPort</a> or <a href="print.openportex">OpenPortEx</a> function supplied.</p>

<p>Typically, a language monitor's <code>WritePort</code> function adds language-specific commands to the data stream contained in the buffer pointed to by <i>pBuffer</i>, and then passes the modified data stream to the port monitor's <code>WritePort</code> function.</p>

<p>A port monitor server DLL's <code>WritePort</code> function usually calls <b>WriteFile</b> (described in the Microsoft Windows SDK documentation) to send the data stream to the kernel-mode port driver.</p>

<p>A typical print job consists of multiple calls to <code>WritePort</code>. Each call can have a different <i>cbBuf</i> value.</p>

<p>The function should return the number of bytes successfully written by placing the number in the location pointed to by <i>pcbWritten</i>. For language monitors, this number must not include the number of extra, language-specific bytes added to the data stream.</p>

<p>The spooler determines the success or failure of the write operation by checking <code>WritePort</code>'s return value, not the returned byte count. So a returned byte count of zero does not represent a failed write unless the function returns <b>FALSE</b>.</p>

<p>Some sort of system-implemented or monitor-implemented time-out mechanism must ensure that the <code>WritePort</code> function will return within a reasonable amount of time, to avoid stalling the spooler.</p>

<p>It is acceptable for a language monitor to call a port monitor's <code>WritePort</code> routine outside of a <a href="print.startdocport">StartDocPort</a>/<a href="print.enddocport">EndDocPort</a> pair. However, some port monitors might fail such a call, so the language monitor must be written to handle this failure.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="..\winsplp\ns-winsplp--monitor2.md">MONITOR2</a>
</dt>
<dt>
<a href="..\winsplp\nf-winsplp-openport.md">OpenPort</a>
</dt>
<dt>
<a href="print.openportex">OpenPortEx</a>
</dt>
<dt>
<a href="print.startdocport">StartDocPort</a>
</dt>
<dt>
<a href="print.enddocport">EndDocPort</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20WritePort function%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
