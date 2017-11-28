---
UID: NS.ndiswwan._NDIS_WWAN_SERVICE_ACTIVATION_STATUS
title: NDIS_WWAN_SERVICE_ACTIVATION_STATUS
author: windows-driver-content
description: The NDIS_WWAN_SERVICE_ACTIVATION_STATUS structure represents the status of service activation on the MB device.
old-location: netvista\ndis_wwan_service_activation_status.htm
old-project: netvista
ms.assetid: 669ef35f-0e59-4ec3-b6cc-5cb2156b51a2
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_WWAN_SERVICE_ACTIVATION_STATUS, NDIS_WWAN_SERVICE_ACTIVATION_STATUS, *PNDIS_WWAN_SERVICE_ACTIVATION_STATUS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndiswwan.h
req.include-header: Ndiswwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WWAN_SERVICE_ACTIVATION_STATUS
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

# NDIS_WWAN_SERVICE_ACTIVATION_STATUS structure



## -description
<p>The NDIS_WWAN_SERVICE_ACTIVATION_STATUS structure represents the status of service activation on the
  MB device.</p>


## -syntax

````
typedef struct _NDIS_WWAN_SERVICE_ACTIVATION_STATUS {
  NDIS_OBJECT_HEADER             Header;
  WWAN_STATUS                    uStatus;
  WWAN_SERVICE_ACTIVATION_STATUS ServiceActivationStatus;
} NDIS_WWAN_SERVICE_ACTIVATION_STATUS, *PNDIS_WWAN_SERVICE_ACTIVATION_STATUS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header with type, revision, and size information about the NDIS_WWAN_SERVICE_ACTIVATION_STATUS
     structure. The MB Service sets the header with the values that are shown in the following table when it
     sends the data structure to the miniport driver for 
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
<p>NDIS_WWAN_SERVICE_ACTIVATION_STATUS_REVISION_1</p>
</td>
</tr>
<tr>
<td>
<p>Size</p>
</td>
<td>
<p>sizeof(NDIS_WWAN_SERVICE_ACTIVATION_STATUS)</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these members, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>uStatus</b>

<dd>
<p>The status of the service activation operation. The following table shows the possible values for
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
<p>Service activation succeeded.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_INVALID_PARAMETERS</p>
</td>
<td>
<p>Service activation failed because of invalid parameters.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_FAILURE</p>
</td>
<td>
<p>Service activation failed. Miniport drivers can return this value if service has already been
        activated.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_PIN_REQUIRED</p>
</td>
<td>
<p>Service activation failed because the device requires a PIN.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_RADIO_POWER_OFF</p>
</td>
<td>
<p>Service activation failed because the radio is currently turned off.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_BAD_SIM</p>
</td>
<td>
<p>Service activation failed because a bad SIM card was detected.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_SIM_NOT_INSERTED</p>
</td>
<td>
<p>Service activation failed because the SIM card was not inserted fully into the device.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_PROVIDER_NOT_VISIBLE</p>
</td>
<td>
<p>Service activation failed because the service provider is not currently visible.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_NO_DEVICE_SUPPORT</p>
</td>
<td>
<p>Service activation failed because the device does not support service activation.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_NOT_INITIALIZED</p>
</td>
<td>
<p>The operation failed because the device is in the process of initializing. Retry the operation
        after the ready-state of the device changes to WwanReadyStateInitialized.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ServiceActivationStatus</b>

<dd>
<p>A formatted 
     <a href="..\wwan\ns-wwan--wwan-service-activation-status.md">
     WWAN_SERVICE_ACTIVATION_STATUS</a> object that represents the status of service activation on the
     device.</p>
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
<p>Available in Windows 7 and later versions of Windows.</p>
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
<a href="..\wwan\ns-wwan--wwan-service-activation-status.md">
   WWAN_SERVICE_ACTIVATION_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_SERVICE_ACTIVATION_STATUS structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
