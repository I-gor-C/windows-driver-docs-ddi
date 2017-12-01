---
UID: NC.wlanihv.DOT11EXTIHV_STOP_POST_ASSOCIATE
title: DOT11EXTIHV_STOP_POST_ASSOCIATE
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extihvstoppostassociate.htm
old-project: netvista
ms.assetid: bd924049-3932-4e85-908e-c3fb488b3a8c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PrintPropertyValue, PrintPropertyValue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wlanihv.h
req.include-header: Wlanihv.h, Windot11.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Dot11ExtIhvStopPostAssociate
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

# DOT11EXTIHV_STOP_POST_ASSOCIATE callback



## -description

## -prototype

````
DOT11EXTIHV_STOP_POST_ASSOCIATE Dot11ExtIhvStopPostAssociate;

DWORD APIENTRY Dot11ExtIhvStopPostAssociate(
  _In_opt_ HANDLE             hIhvExtAdapter,
  _In_     PDOT11_MAC_ADDRESS pPeer,
  _In_     DOT11_ASSOC_STATUS dot11AssocStatus
)
{ ... }
````


## -parameters
<dl>

### -param <i>hIhvExtAdapter</i> [in, optional]

<dd>
<p>The handle used by the IHV Extensions DLL to reference the wireless LAN (WLAN) adapter. This
     handle value was specified through a previous call to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a> IHV
     Handler function.</p>
</dd>

### -param <i>pPeer</i> [in]

<dd>
<p>A pointer to a 
     <a href="..\windot11\ns-windot11--dot11-mac-address.md">DOT11_MAC_ADDRESS</a> structure, which
     contains the media access control (MAC) of the access point (AP) with which the IHV Extensions DLL
     initiated a post-association operation.
     </p>
<div class="alert"><b>Note</b>  For Windows Vista, the IHV Extensions DLL supports only infrastructure basic
     service set (BSS) networks.</div>
<div> </div>
</dd>

### -param <i>dot11AssocStatus</i> [in]

<dd>
<p>A 
     <a href="netvista.dot11_assoc_status">DOT11_ASSOC_STATUS</a> type that specifies the
     association status of the 802.11 station to the network.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.</p>

## -remarks
<p>The operating system calls the 
    <i>Dot11ExtIhvStopPostAssociate</i> function to cancel the post-association operation whenever one of the
    following occurs.</p>

<p>The WLAN adapter completes a disassociation operation with the AP. In this situation, the Native
      802.11 miniport driver, which manages the adapter, makes a media-specific 
      <a href="netvista.ndis_status_dot11_disassociation">
      NDIS_STATUS_DOT11_DISASSOCIATION</a> indication. For more information about the disassociation
      operation, see 
      <a href="NULL">Disassociation Operations</a>.</p>

<p>The WLAN adapter is disabled or removed. In this situation, the operating system calls the 
      <i>Dot11ExtIhvStopPostAssociate</i> function before it calls the 
      <a href="..\wlanihv\nc-wlanihv-dot11extihv-deinit-adapter.md">
      Dot11ExtIhvDeinitAdapter</a> function.</p>

<p>The operating system calls the 
    <i>Dot11ExtIhvStopPostAssociate</i> function to notify the IHV Extensions DLL that the data port created
    for the association is down. The operating system calls this function regardless of whether the DLL has
    completed the post-association operation through a call to 
    <a href="..\wlanihv\nc-wlanihv-dot11ext-post-associate-completion.md">
    Dot11ExtPostAssociateCompletion</a>.</p>

<p>For more information about the post-association operation, see 
    <a href="NULL">Post-Association Operations</a>.</p>

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
<dt>Wlanihv.h (include Wlanihv.h or Windot11.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.dot11_assoc_status">DOT11_ASSOC_STATUS</a>
</dt>
<dt>
<a href="..\windot11\ns-windot11--dot11-mac-address.md">DOT11_MAC_ADDRESS</a>
</dt>
<dt>
<a href="netvista.ndis_status_dot11_disassociation">
   NDIS_STATUS_DOT11_DISASSOCIATION</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-deinit-adapter.md">Dot11ExtIhvDeinitAdapter</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-perform-post-associate.md">
   Dot11ExtIhvPerformPostAssociate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXTIHV_STOP_POST_ASSOCIATE callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
