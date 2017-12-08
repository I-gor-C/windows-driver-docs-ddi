---
UID: NF.winsplp.ReadPort
title: ReadPort function
author: windows-driver-content
description: A port monitor's ReadPort function reads data from a printer port.
old-location: print\readport.htm
old-project: print
ms.assetid: ab1fb259-edcb-4e19-9afb-18aa6688764a
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: ReadPort
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
req.alt-api: ReadPort
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
req.product: Windows 10 or later.
---

# ReadPort function



## -description
A port monitor's <code>ReadPort</code> function reads data from a printer port.


## -syntax

````
BOOL ReadPort(
  _In_  HANDLE  hPort,
  _Out_ LPBYTE  pBuffer,
        DWORD   cbBuffer,
  _Out_ LPDWORD pcbRead
);
````


## -parameters

### -param hPort [in]

Caller-supplied port handle.

### -param pBuffer [out]

Caller-supplied pointer to a buffer to receive data read from the port.

### -param cbBuffer 

Caller-supplied size, in bytes, of <i>pBuffer</i>.

### -param pcbRead [out]

Caller-supplied pointer to a location to receive the number of bytes successfully read from the port.

## -returns
If the operation succeeds, the function should return <b>TRUE</b>. Otherwise it should return <b>FALSE</b>.

## -remarks

<a href="https://msdn.microsoft.com/26ba1c22-390a-4187-b67a-3f3497964f8e">Language monitors</a> and port monitor server DLLs are required to define a <code>ReadPort</code> function and include the function's address in a <a href="print.monitor2">MONITOR2</a> structure.

The handle received as the function's <i>hPort</i> argument is the port handle that the monitor's <a href="print.openport">OpenPort</a> or <a href="print.openportex">OpenPortEx</a> function supplied.

Typically, a language monitor's <code>ReadPort</code> function calls the associated port monitor's <code>ReadPort</code> function, and returns the obtained buffer contents to the caller.

Additionally, a language monitor might create a separate thread that calls the port monitor's <code>ReadPort</code> function to check for unsolicited status information. If such a read operation succeeds, the status information should be returned to the spooler by calling <b>SetPort</b> (described in the Microsoft Windows SDK documentation).

Typically, a port monitor server DLL's <code>ReadPort</code> function calls <b>ReadFile</b> (described in the Windows SDK documentation) to obtain data from the kernel-mode port driver. The function just returns the data to the caller.

Even though both language monitors and port monitors must define <code>ReadPort</code> functions and place their addresses in MONITOR2 structures, a language monitor's <code>ReadPort</code> function is never actually called by the spooler or an application. The function is solely for the internal use of the language monitor itself.

For example pjlmon.dll, the <a href="https://msdn.microsoft.com/fd1ef790-c17b-4735-87fc-6b7b8597ac4d">sample language monitor</a>, creates a separate thread that calls its own <code>ReadPort</code> to watch for unsolicited printer status information, and the <code>ReadPort</code> function calls the port monitor's <code>ReadPort</code> function. When the port monitor returns data to the language monitor, the language monitor parses the received data and calls <b>SetPort</b> (described in the Windows SDK documentation) to send status information to the spooler.

The function should return the number of bytes successfully read by placing the number in the location pointed to by <i>pcbRead</i>. The caller determines the success or failure of the write operation by checking <code>ReadPort's</code> return value, not the returned byte count. So a returned byte count of zero does not represent a failed read unless the function returns <b>FALSE</b>.

Some sort of system-implemented or monitor-implemented time-out mechanism must ensure that the <code>ReadPort</code> function will return within a reasonable amount of time, to avoid stalling the spooler.

It is acceptable for a language monitor to call a port monitor's <code>ReadPort</code> routine outside of a <a href="print.startdocport">StartDocPort</a>/<a href="print.enddocport">EndDocPort</a> pair. (Such a call might be generated by a thread checking for unsolicited status.) However, some port monitors might fail such a call, so the language monitor must be written to handle this failure.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
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
<a href="print.getprinterdatafromport">GetPrinterDataFromPort</a>
</dt>
<dt>
<a href="print.openport">OpenPort</a>
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
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20ReadPort function%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>