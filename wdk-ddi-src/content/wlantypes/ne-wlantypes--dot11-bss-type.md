---
UID: NE.wlantypes._DOT11_BSS_TYPE
title: DOT11_BSS_TYPE
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_bss_type.htm
ms.assetid: 5cb263e2-e5b7-456f-9fef-deaf5434c404
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: wlantypes.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_BSS_TYPE
req.alt-loc: wlantypes.h
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
ms.keywords: DOT11_MSONEX_RESULT_PARAMS, DOT11_MSONEX_RESULT_PARAMS, *PDOT11_MSONEX_RESULT_PARAMS
req.iface: 
req.product: Windows 10 or later.
---

# DOT11_BSS_TYPE enumeration



## -description

## -syntax

````
typedef enum _DOT11_BSS_TYPE { 
  dot11_BSS_type_infrastructure  = 1,
  dot11_BSS_type_independent     = 2,
  dot11_BSS_type_any             = 3
} DOT11_BSS_TYPE, *PDOT11_BSS_TYPE;
````


## -enum-fields
<dl>

### -field <a id="dot11_BSS_type_infrastructure"></a><a id="dot11_bss_type_infrastructure"></a><a id="DOT11_BSS_TYPE_INFRASTRUCTURE"></a><b>dot11_BSS_type_infrastructure</b>

<dd>
<p>Specifies an infrastructure BSS network.</p>
</dd>

### -field <a id="dot11_BSS_type_independent"></a><a id="dot11_bss_type_independent"></a><a id="DOT11_BSS_TYPE_INDEPENDENT"></a><b>dot11_BSS_type_independent</b>

<dd>
<p>Specifies an independent BSS (IBSS) network.</p>
</dd>

### -field <a id="dot11_BSS_type_any"></a><a id="dot11_bss_type_any"></a><a id="DOT11_BSS_TYPE_ANY"></a><b>dot11_BSS_type_any</b>

<dd>
<p>Specifies either infrastructure or IBSS network.</p>
</dd>
</dl>

## -remarks
<p>The 
    <b>dot11_BSS_type_any</b> enumerator is valid only if it is specified when 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569413">OID_DOT11_SCAN_REQUEST</a> is set. 
    <b>dot11_BSS_type_any</b> is used to request a scan for all types of BSSs that are visible to the 802.11
    station.</p>

<p>The 
    <b>dot11_BSS_type_any</b> enumerator is valid only if it is specified when 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569413">OID_DOT11_SCAN_REQUEST</a> is set. 
    <b>dot11_BSS_type_any</b> is used to request a scan for all types of BSSs that are visible to the 802.11
    station.</p>

<p>The 
    <b>dot11_BSS_type_any</b> enumerator is valid only if it is specified when 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569413">OID_DOT11_SCAN_REQUEST</a> is set. 
    <b>dot11_BSS_type_any</b> is used to request a scan for all types of BSSs that are visible to the 802.11
    station.</p>

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
<dt>Wlantypes.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547630">DOT11EXT_IHV_PROFILE_PARAMS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547665">DOT11_BSS_ENTRY</a>
</dt>
<dt>
<a href="netvista.ndis_status_dot11_connection_start">
   NDIS_STATUS_DOT11_CONNECTION_START</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569142">OID_DOT11_DESIRED_BSS_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569360">OID_DOT11_ENUM_BSS_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569413">OID_DOT11_SCAN_REQUEST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_BSS_TYPE enumeration%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
