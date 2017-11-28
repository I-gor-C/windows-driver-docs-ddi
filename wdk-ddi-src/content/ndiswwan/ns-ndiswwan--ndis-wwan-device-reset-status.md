---
UID: NS.ndiswwan._NDIS_WWAN_DEVICE_RESET_STATUS
title: NDIS_WWAN_DEVICE_RESET_STATUS
author: windows-driver-content
description: The NDIS_WWAN_DEVICE_RESET_STATUS structure represents a modem device's reset status. It is sent to the MB host in the NDIS_STATUS_WWAN_DEVICE_RESET_STATUS notification in an asynchronous response to an OID_WWAN_DEVICE_RESET set request.
old-location: netvista\ndis_wwan_device_reset_status.htm
old-project: netvista
ms.assetid: D18E8633-BEAD-49A5-A730-10564AFF8A3E
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_WWAN_DEVICE_RESET_STATUS, NDIS_WWAN_DEVICE_RESET_STATUS, *PNDIS_WWAN_DEVICE_RESET_STATUS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndiswwan.h
req.include-header: Ndiswwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WWAN_DEVICE_RESET_STATUS
req.alt-loc: ndiswwan.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NDIS_WWAN_DEVICE_RESET_STATUS structure



## -description
<p>The <b>NDIS_WWAN_DEVICE_RESET_STATUS</b>  structure represents a modem device's reset status. It is sent to the MB host in the <a href="https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-wwan-device-reset-status">NDIS_STATUS_WWAN_DEVICE_RESET_STATUS</a> notification in an asynchronous response to an <a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-device-reset">OID_WWAN_DEVICE_RESET</a> set request.</p>


## -syntax

````
typedef struct _NDIS_WWAN_DEVICE_RESET_STATUS {
  NDIS_OBJECT_HEADER Header;
  WWAN_STATUS        uStatus;
} NDIS_WWAN_DEVICE_RESET_STATUS, *PNDIS_WWAN_DEVICE_RESET_STATUS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header with type, revision, and size information about the <b>NDIS_WWAN_DEVICE_RESET_STATUS</b> structure.
     The MB Service sets the header with the values that are shown in the following table when it sends the
     data structure to the miniport driver for 
     <i>set</i> operations. Miniport drivers must set the header with the same values when they send the data
     structure to the MB service.
     </p>
<table>
<tr>
<th>Header submember</th>
<th>Value</th>
</tr>
<tr>
<td>
<p>Type</p>
</td>
<td>
<p>NDIS_OBJECT_TYPE_DEFAULT</p>
</td>
</tr>
<tr>
<td>
<p>Revision</p>
</td>
<td>
<p>NDIS_WWAN_DEVICE_RESET_STATUS_REVISION_1</p>
</td>
</tr>
<tr>
<td>
<p>Size</p>
</td>
<td>
<p>sizeof(NDIS_WWAN_DEVICE_RESET_STATUS)</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these members, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>uStatus</b>

<dd>
<p>The status of system capability. The following table shows the possible values for
     this member.
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_STATUS_SUCCESS</p>
</td>
<td>
<p>The operation succeeded.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_BUSY</p>
</td>
<td>
<p>The operation failed because the device was busy. In the absence of any explicit information from the function to clear this condition, the host can use subsequent actions by the function (e.g. notifications or command completions) as a hint to retry the failed operation.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_FAILURE</p>
</td>
<td>
<p>The operation failed.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_NO_DEVICE_SUPPORT</p>
</td>
<td>
<p>The operation failed because the device does not support this OID.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndiswwan.h (include Ndiswwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-wwan-device-reset-status">NDIS_STATUS_WWAN_DEVICE_RESET_STATUS</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-device-reset">OID_WWAN_DEVICE_RESET</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/mb-modem-reset-operations">MB modem reset operations</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_DEVICE_RESET_STATUS structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
