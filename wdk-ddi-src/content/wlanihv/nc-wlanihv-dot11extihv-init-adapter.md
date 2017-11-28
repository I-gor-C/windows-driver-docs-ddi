---
UID: NC.wlanihv.DOT11EXTIHV_INIT_ADAPTER
title: DOT11EXTIHV_INIT_ADAPTER
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extihvinitadapter.htm
old-project: netvista
ms.assetid: 96dc1718-ee35-440a-94e8-eba4a41c9559
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
req.alt-api: Dot11ExtIhvInitAdapter
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

# DOT11EXTIHV_INIT_ADAPTER callback



## -description

## -prototype

````
DOT11EXTIHV_INIT_ADAPTER Dot11ExtIhvInitAdapter;

DWORD APIENTRY Dot11ExtIhvInitAdapter(
  _In_     PDOT11_ADAPTER pDot11Adapter,
  _In_opt_ HANDLE         hDot11SvcHandle,
  _Out_    PHANDLE        phIhvExtAdapter
)
{ ... }
````


## -parameters
<dl>

### -param <i>pDot11Adapter</i> [in]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff547643">DOT11_ADAPTER</a> structure, which identifies the
     adapter to be initialized.</p>
</dd>

### -param <i>hDot11SvcHandle</i> [in, optional]

<dd>
<p>A handle assigned by the operating system for the adapter. The IHV Extensions DLL must use this
     handle value when calling any IHV Extensibility function that declares an 
     <i>hDot11SvcHandle</i> parameter, such as 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-pre-associate-completion.md">
     Dot11ExtPreAssociateCompletion</a>.</p>
</dd>

### -param <i>phIhvExtAdapter</i> [out]

<dd>
<p>A pointer to a handle variable. The IHV Extensions DLL must assign a unique handle value for the
     adapter and set *
     <i>phIhvExtAdapter</i> to the handle value. The operating system uses this handle value when it calls any
     IHV Handler function that declares an 
     <i>hIhvExtAdapter</i> parameter, such as 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-perform-pre-associate.md">
     Dot11ExtIhvPerformPreAssociate</a>. 
     </p>
<p>Typically, the IHV Extensions DLL allocates a state array for the adapter context and returns the
     address of the array as the handle value.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.</p>

## -remarks
<p>The operating system calls the 
    <i>Dot11ExtIhvInitAdapter</i> function whenever a WLAN adapter becomes available and enabled for use, such
    as when a PCMCIA adapter is inserted.</p>

<p>For more information about WLAN adapter initialization, see 
    <a href="NULL">802.11 WLAN Adapter Arrival</a>.</p>

<p>The operating system calls the 
    <i>Dot11ExtIhvInitAdapter</i> function whenever a WLAN adapter becomes available and enabled for use, such
    as when a PCMCIA adapter is inserted.</p>

<p>For more information about WLAN adapter initialization, see 
    <a href="NULL">802.11 WLAN Adapter Arrival</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547643">DOT11_ADAPTER</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-pre-associate-completion.md">
   Dot11ExtPreAssociateCompletion</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-perform-pre-associate.md">
   Dot11ExtIhvPerformPreAssociate</a>
</dt>
<dt>
<a href="netvista.native_802_11_ihv_extensibility_functions">Native 802.11 IHV
   Extensibility Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXTIHV_INIT_ADAPTER callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
