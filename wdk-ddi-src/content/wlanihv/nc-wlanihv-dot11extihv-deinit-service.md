---
UID: NC.wlanihv.DOT11EXTIHV_DEINIT_SERVICE
title: DOT11EXTIHV_DEINIT_SERVICE
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extihvdeinitservice.htm
old-project: netvista
ms.assetid: 5ee52306-4229-4d81-af1f-6eb37f41ad41
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PrintPropertyValue, PrintPropertyValue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wlanihv.h
req.include-header: Wlanihv.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Dot11ExtIhvDeinitService
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
req.iface: 
req.product: Windows 10 or later.
---

# DOT11EXTIHV_DEINIT_SERVICE callback



## -description

## -prototype

````
DOT11EXTIHV_DEINIT_SERVICE Dot11ExtIhvDeinitService;

VOID APIENTRY Dot11ExtIhvDeinitService(
   VOID 
)
{ ... }
````


## -parameters
<dl>

### -param <i></i> 

<dd>
<p>None</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>When the 
    <i>Dot11ExtIhvDeinitService</i> function is called, the IHV Extensions DLL must be brought to a state that
    it can safely be unloaded by the operating system. The DLL must follow these guidelines when this
    function is called.</p>

<p>The operating system calls the 
      <a href="..\wlanihv\nc-wlanihv-dot11extihv-deinit-adapter.md">
      Dot11ExtIhvDeinitAdapter</a> function prior to calling the 
      <i>Dot11ExtIhvDeinitService</i> function. As a result, the 
      <i>Dot11ExtIhvDeinitService</i> function should not initiate any operations on the WLAN adapter.
      Instead, 
      <i>Dot11ExtIhvDeinitService</i> should prepare the DLL to be unloaded by the operating system.</p>

<p>The DLL must terminate all executing threads that it created. The DLL must not return from the 
      <i>Dot11ExtIhvDeinitService</i> function call until all threads have been terminated.</p>

<p>The DLL must free any allocated resources for the DLL itself. In particular, all memory the DLL
      allocated through calls to 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff547419">Dot11ExtAllocateBuffer</a> must be
      freed through calls to 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff547422">Dot11ExtFreeBuffer</a>.</p>

<p>When the 
    <i>Dot11ExtIhvDeinitService</i> function is called, the IHV Extensions DLL must be brought to a state that
    it can safely be unloaded by the operating system. The DLL must follow these guidelines when this
    function is called.</p>

<p>The operating system calls the 
      <a href="..\wlanihv\nc-wlanihv-dot11extihv-deinit-adapter.md">
      Dot11ExtIhvDeinitAdapter</a> function prior to calling the 
      <i>Dot11ExtIhvDeinitService</i> function. As a result, the 
      <i>Dot11ExtIhvDeinitService</i> function should not initiate any operations on the WLAN adapter.
      Instead, 
      <i>Dot11ExtIhvDeinitService</i> should prepare the DLL to be unloaded by the operating system.</p>

<p>The DLL must terminate all executing threads that it created. The DLL must not return from the 
      <i>Dot11ExtIhvDeinitService</i> function call until all threads have been terminated.</p>

<p>The DLL must free any allocated resources for the DLL itself. In particular, all memory the DLL
      allocated through calls to 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff547419">Dot11ExtAllocateBuffer</a> must be
      freed through calls to 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff547422">Dot11ExtFreeBuffer</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547419">Dot11ExtAllocateBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547422">Dot11ExtFreeBuffer</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-deinit-adapter.md">Dot11ExtIhvDeinitAdapter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXTIHV_DEINIT_SERVICE callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
