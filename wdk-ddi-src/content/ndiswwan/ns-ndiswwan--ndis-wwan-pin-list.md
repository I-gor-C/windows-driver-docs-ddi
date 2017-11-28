---
UID: NS.ndiswwan._NDIS_WWAN_PIN_LIST
title: NDIS_WWAN_PIN_LIST
author: windows-driver-content
description: The NDIS_WWAN_PIN_LIST structure represents a list of descriptions of Personal Identification Numbers (PINs).
old-location: netvista\ndis_wwan_pin_list.htm
old-project: netvista
ms.assetid: 1d3c1084-8f51-4c8a-813e-6700d60c3dab
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_WWAN_PIN_LIST, NDIS_WWAN_PIN_LIST, *PNDIS_WWAN_PIN_LIST
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
req.alt-api: NDIS_WWAN_PIN_LIST
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

# NDIS_WWAN_PIN_LIST structure



## -description
<p>The NDIS_WWAN_PIN_LIST structure represents a list of descriptions of Personal Identification Numbers
  (PINs).</p>


## -syntax

````
typedef struct _NDIS_WWAN_PIN_LIST {
  NDIS_OBJECT_HEADER Header;
  WWAN_STATUS        uStatus;
  WWAN_PIN_LIST      PinList;
} NDIS_WWAN_PIN_LIST, *PNDIS_WWAN_PIN_LIST;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header with type, revision, and size information about the NDIS_WWAN_PIN_LIST structure. The
     MB Service sets the header with the values that are shown in the following table when it sends the data
     structure to the miniport driver for 
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
<p>NDIS_WWAN_PIN_LIST_REVISION_1</p>
</td>
</tr>
<tr>
<td>
<p>Size</p>
</td>
<td>
<p>sizeof(NDIS_WWAN_PIN_LIST)</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these members, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>uStatus</b>

<dd>
<p>The status of the PIN list operation. The following table shows the possible values for this.
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
<p>The PIN list operation succeeded.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_FAILURE</p>
</td>
<td>
<p>The PIN list operation failed.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_PIN_REQUIRED</p>
</td>
<td>
<p>The PIN list operation failed because a PIN must be entered before this operation can proceed.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_SIM_NOT_INSERTED</p>
</td>
<td>
<p>The PIN list operation failed because the SIM card is not inserted.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_NOT_INITIALIZED</p>
</td>
<td>
<p>The operation failed because the device is in the process of initializing. Retry the operation
        after the ready-state of the device changes to 
        <b>WwanReadyStateInitialized</b>.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_BAD_SIM</p>
</td>
<td>
<p>The operation failed because a bad SIM card was detected.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>PinList</b>

<dd>
<p>A formatted 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571217">WWAN_PIN_LIST</a> object that represents a list
     of descriptions of Personal Identification Numbers (PINs).</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571217">WWAN_PIN_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_PIN_LIST structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
