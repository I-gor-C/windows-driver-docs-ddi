---
UID: NF.winsplp.UpdatePrintDeviceObject
title: UpdatePrintDeviceObject
author: windows-driver-content
description: The UpdatePrintDeviceObject function updates the properties of a device object that is in the print provider queue.
old-location: print\updateprintdeviceobject.htm
old-project: print
ms.assetid: 52E8F8BF-0362-4BA9-BABD-7B009B3FFA7F
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: UpdatePrintDeviceObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winsplp.h
req.include-header: Winspool.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UpdatePrintDeviceObject
req.alt-loc: WinSpool.drv
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: WinSpool.lib
req.dll: WinSpool.drv
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# UpdatePrintDeviceObject function



## -description

## -syntax

````
HRESULT WINAPI UpdatePrintDeviceObject(
  _In_ HANDLE hPrinter,
  _In_ HANDLE hDeviceObject
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> [in]

<dd>
<p>The HANDLE to an open printer. This should be a handle that was returned by the <b>AddPrinter</b> or <b>OpenPrinter</b> spooler functions.</p>
</dd>

### -param <i>hDeviceObject</i> [in]

<dd>
<p>The HANDLE to the device object to be updated. This should be a device object that was created with <a href="https://msdn.microsoft.com/library/windows/hardware/dn917890">AddPrintDeviceObject</a>.</p>
</dd>
</dl>

## -returns
<p>The <b>UpdatePrintDeviceObject</b> function returns S_OK, if the properties of the  device object were updated successfully. Otherwise it returns an error.</p>

<p>For example, this function can return HRESULT_FROM_WIN32(ERROR_INVALID_HANDLE), if the function call was made with an invalid HANDLE, or the device object was removed before the function call was made.</p>

## -remarks
<p>The <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd162845(v=vs.85).aspx">PRINTER_INFO_2</a>  structure is a good example of the kind of properties that <b>UpdatePrintDeviceObject</b> can update.</p>

<p>The <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd162845(v=vs.85).aspx">PRINTER_INFO_2</a>  structure is a good example of the kind of properties that <b>UpdatePrintDeviceObject</b> can update.</p>

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
<dt>Winsplp.h (include Winspool.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>WinSpool.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WinSpool.drv</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn917890">AddPrintDeviceObject</a>
</dt>
<dt><a href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd162845(v=vs.85).aspx">PRINTER_INFO_2</a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20UpdatePrintDeviceObject function%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
