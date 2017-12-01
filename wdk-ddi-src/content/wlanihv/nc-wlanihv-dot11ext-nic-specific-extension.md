---
UID: NC.wlanihv.DOT11EXT_NIC_SPECIFIC_EXTENSION
title: DOT11EXT_NIC_SPECIFIC_EXTENSION
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extnicspecificextension.htm
old-project: netvista
ms.assetid: e588db31-d6d7-4b79-80f5-128c6d618ab6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PrintPropertyValue, PrintPropertyValue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wlanihv.h
req.include-header: Wlanihv.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Dot11ExtNicSpecificExtension
req.alt-loc: wlanihv.h
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

# DOT11EXT_NIC_SPECIFIC_EXTENSION callback



## -description

## -prototype

````
DWORD WINAPI * Dot11ExtNicSpecificExtension(
  _In_opt_ HANDLE hDot11SvcHandle,
  _In_     DWORD  dwInBufferSize,
  _In_     LPVOID pvInBuffer,
  _Inout_  DWORD  *pdwOutBufferSize,
  _Out_    LPVOID pvOutBuffer
);
````


## -parameters
<dl>

### -param <i>hDot11SvcHandle</i> [in, optional]

<dd>
<p>The handle used by the operating system to reference the WLAN adapter. This handle value was
     specified through a previous call to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a> IHV
     Handler function.</p>
</dd>

### -param <i>dwInBufferSize</i> [in]

<dd>
<p>The size, in bytes, of the caller-allocated data buffer referenced by the 
     <i>pvInBuffer</i> parameter.</p>
</dd>

### -param <i>pvInBuffer</i> [in]

<dd>
<p>A pointer to a caller-allocated input buffer that contains the data required to perform the
     operation. The format of this data is defined by the IHV.</p>
</dd>

### -param <i>pdwOutBufferSize</i> [in, out]

<dd>
<p>A pointer to a caller-allocated DWORD variable. When the 
     <b>Dot11ExtNicSpecificExtension</b> function is called, the IHV Extensions DLL
     must set this variable to the size, in bytes, of the caller-allocated data buffer referenced by the 
     <i>pvOutBuffer</i> parameter. When the function returns, the operating system sets the variable to the
     actual number of bytes returned in the data buffer referenced by the 
     <i>pvOutBuffer</i> parameter.</p>
</dd>

### -param <i>pvOutBuffer</i> [out]

<dd>
<p>A pointer to a caller-allocated buffer that contains data returned from the Native 802.11 miniport
     driver for the specified request. The format of this data is defined by the IHV. This parameter can be
     <b>NULL</b> if data is not to be returned by the Native 802.11 miniport driver.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.</p>

## -remarks
<p>The 
    <b>Dot11ExtNicSpecificExtension</b> function allows the IHV Extensions DLL to
    pass proprietary method requests to the Native 802.11 miniport driver, which is referenced by the 
    <i>hDot11SvcHandle</i> parameter. The operating system issues the method request through the Native 802.11
    
    <a href="netvista.oid_dot11_nic_specific_extension">
    OID_DOT11_NIC_SPECIFIC_EXTENSION</a> object identifier (OID).</p>

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
<a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a>
</dt>
<dt>
<a href="netvista.oid_dot11_nic_specific_extension">
   OID_DOT11_NIC_SPECIFIC_EXTENSION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXT_NIC_SPECIFIC_EXTENSION callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
