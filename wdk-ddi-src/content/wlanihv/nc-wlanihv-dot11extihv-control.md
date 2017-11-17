---
UID: NC.wlanihv.DOT11EXTIHV_CONTROL
title: DOT11EXTIHV_CONTROL
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extihvcontrol.htm
ms.assetid: 27e1f112-a961-4464-9048-b56394930453
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: wlanihv.h
req.include-header: Wlanihv.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Dot11ExtIhvControl
req.alt-loc: Wlanihv.h
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
ms.keywords: PrintPropertyValue, PrintPropertyValue
req.iface: 
req.product: Windows 10 or later.
---

# DOT11EXTIHV_CONTROL callback



## -description

## -prototype

````
DOT11EXTIHV_CONTROL Dot11ExtIhvControl;

DWORD APIENTRY Dot11ExtIhvControl(
  _In_opt_  HANDLE hIhvExtAdapter,
  _In_      DWORD  dwInBufferSize,
  _In_opt_  PBYTE  pInBuffer,
  _In_      DWORD  dwOutBufferSize,
  _Out_opt_ PBYTE  pOutBuffer,
  _Out_     DWORD  pdwBytesReturned
)
{ ... }
````


## -parameters
<dl>

### -param <i>hIhvExtAdapter</i> [in, optional]

<dd>
<p>The handle used by the IHV Extensions DLL to reference the WLAN adapter. This handle value was
     specified through a previous call to the 
     <a href="https://msdn.microsoft.com/96dc1718-ee35-440a-94e8-eba4a41c9559">Dot11ExtIhvInitAdapter</a> IHV Handler function.</p>
</dd>

### -param <i>dwInBufferSize</i> [in]

<dd>
<p>The size, in bytes, of the input control buffer pointed to by the 
     <i>pInBuffer</i> parameter.</p>
</dd>

### -param <i>pInBuffer</i> [in, optional]

<dd>
<p>A pointer to the input control buffer.</p>
</dd>

### -param <i>dwOutBufferSize</i> [in]

<dd>
<p>The size, in bytes, of the output buffer (if provided) pointed to by the 
     <i>pOutBuffer</i> parameter.</p>
</dd>

### -param <i>pOutBuffer</i> [out, optional]

<dd>
<p>A pointer to the output buffer, if provided.</p>
</dd>

### -param <i>pdwBytesReturned</i> [out]

<dd>
<p>A pointer to a variable that contains the size, in bytes, of the response input/output
     buffer.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.</p>

## -remarks
<p>The operating system calls this function when the 
    <b>WlanIhvControl</b> function is called with the 
    <i>Type</i> parameter set to a value of 
    <b>wlan_ihv_control_type_service</b>. For a description of the 
    <b>WlanIhvControl</b> function, see the Microsoft Windows SDK documentation.</p>

<p>Data transferred with this function is not validated, so the IHV is responsible for correctly parsing
    the input buffer.</p>

<p>The data buffer pointed to by the 
    <i>pdwBytesReturned</i> parameter will always be returned. However, the buffer pointed to by 
    <i>pOutBuffer</i> will be copied only if a valid pointer is provided and the value pointed to by 
    <i>pdwBytesReturned</i> is less than or equal to 
    <i>dwOutBufferSize</i> .</p>

<p>The operating system calls this function when the 
    <b>WlanIhvControl</b> function is called with the 
    <i>Type</i> parameter set to a value of 
    <b>wlan_ihv_control_type_service</b>. For a description of the 
    <b>WlanIhvControl</b> function, see the Microsoft Windows SDK documentation.</p>

<p>Data transferred with this function is not validated, so the IHV is responsible for correctly parsing
    the input buffer.</p>

<p>The data buffer pointed to by the 
    <i>pdwBytesReturned</i> parameter will always be returned. However, the buffer pointed to by 
    <i>pOutBuffer</i> will be copied only if a valid pointer is provided and the value pointed to by 
    <i>pdwBytesReturned</i> is less than or equal to 
    <i>dwOutBufferSize</i> .</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wlanihv.h (include Wlanihv.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/96dc1718-ee35-440a-94e8-eba4a41c9559">Dot11ExtIhvInitAdapter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXTIHV_CONTROL callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
