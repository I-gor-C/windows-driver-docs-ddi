---
UID: NS.wlclient._DOT11_BSS_LIST
title: DOT11_BSS_LIST
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_bss_list.htm
old-project: netvista
ms.assetid: e5c31c4d-8c46-4af1-90de-0311cc90c6c0
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11_BSS_LIST, DOT11_BSS_LIST, *PDOT11_BSS_LIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wlclient.h
req.include-header: Wlclient.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_BSS_LIST
req.alt-loc: wlclient.h
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

# DOT11_BSS_LIST structure



## -description

## -syntax

````
typedef struct _DOT11_BSS_LIST {
  ULONG  uNumOfBytes;
  PUCHAR pucBuffer;
} DOT11_BSS_LIST, *PDOT11_BSS_LIST;
````


## -struct-fields
<dl>

### -field <b>uNumOfBytes</b>

<dd>
<p>The length, in bytes, of the data within the buffer referenced by the 
     <b>pucBuffer</b> member.</p>
</dd>

### -field <b>pucBuffer</b>

<dd>
<p>A pointer to a buffer that contains a list of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff547665">DOT11_BSS_ENTRY</a> structures. Each
     DOT11_BSS_ENTRY structure specifies a single 802.11 Beacon and Probe Response frame.
     </p>
<p>The DOT11_BSS_ENTRY structure has a variable length. However, each entry within the list of
     DOT11_BSS_ENTRY structures does not contain padding for the alignment of the next entry in the
     list.</p>
</dd>
</dl>

## -remarks
<p>The 802.11 Beacon and Probe Response frames within the 
    <b>pucBuffer</b> member were received from the underlying 802.11 station during its previous scan
    operation. For more information about this operation, see 
    <a href="netvista.native_802_11_scan_operations">Native 802.11 Scan
    Operations</a>.</p>

## -requirements
<table>
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
<dt>Wlclient.h (include Wlclient.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547665">DOT11_BSS_ENTRY</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-create-discovery-profiles.md">
   Dot11ExtIhvCreateDiscoveryProfiles</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-perform-capability-match.md">
   Dot11ExtIhvPerformCapabilityMatch</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-perform-pre-associate.md">
   Dot11ExtIhvPerformPreAssociate</a>
</dt>
<dt>
<a href="netvista.native_802_11_ihv_handler_functions">Native 802.11 IHV Handler
   Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_BSS_LIST structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
