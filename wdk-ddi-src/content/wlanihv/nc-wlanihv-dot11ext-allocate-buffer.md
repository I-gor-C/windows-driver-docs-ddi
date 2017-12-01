---
UID: NC.wlanihv.DOT11EXT_ALLOCATE_BUFFER
title: DOT11EXT_ALLOCATE_BUFFER
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extallocatebuffer.htm
old-project: netvista
ms.assetid: 22c61f1d-027c-4e3e-af34-c513d4e1d0cc
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
req.alt-api: Dot11ExtAllocateBuffer
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

# DOT11EXT_ALLOCATE_BUFFER callback



## -description

## -prototype

````
DWORD WINAPI * Dot11ExtAllocateBuffer(
  _In_  DWORD  dwByteCount,
  _Out_ LPVOID *ppvBuffer
);
````


## -parameters
<dl>

### -param <i>dwByteCount</i> [in]

<dd>
<p>Size, in bytes, of the buffer to allocate.</p>
</dd>

### -param <i>ppvBuffer</i> [out]

<dd>
<p>A pointer to a caller-supplied variable that stores the address of the allocated buffer. The 
     <i>ppvBuffer</i> parameter has a valid non-null value if the return value is ERROR_SUCCESS.</p>
</dd>
</dl>

## -returns
<p>The call returns an ERROR_xxxx code defined in 
     Winerror.h. The following ERROR_xxxx codes are commonly returned by the 
     <b>Dot11ExtAllocateBuffer</b> function.</p><dl>
<dt><b>ERROR_SUCCESS</b></dt>
</dl><p>The call succeeded without an error.</p><dl>
<dt><b>ERROR_OUTOFMEMORY</b></dt>
</dl><p>The operating system was unable to allocate the memory due to a lack of resources.</p>

<p> </p>

## -remarks
<p>The IHV Extensions DLL must follow these guidelines when calling the 
    <b>Dot11ExtAllocateBuffer</b> function.</p>

<p>The IHV Extensions DLL must call this function when returning any variable-length buffer from an IHV
      Handler function. In this situation, the operating system is responsible for freeing the buffer after
      the return of the IHV Handler function.</p>

<p>For more information about the IHV Handler functions, see 
      <a href="netvista.native_802_11_ihv_handler_functions">Native 802.11 IHV Handler
      Functions</a>.</p>

<p>The IHV Extensions DLL might call this function to allocate memory referenced by the DLL itself.
     </p>

<p>In this situation, the DLL must free the memory buffer by calling 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-free-buffer.md">Dot11ExtFreeBuffer</a>.</p>

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
<a href="..\wlanihv\nc-wlanihv-dot11ext-free-buffer.md">Dot11ExtFreeBuffer</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-create-discovery-profiles.md">
   Dot11ExtIhvCreateDiscoveryProfiles</a>
</dt>
<dt>
<a href="netvista.native_802_11_ihv_handler_functions">Native 802.11 IHV Handler
   Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXT_ALLOCATE_BUFFER callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
