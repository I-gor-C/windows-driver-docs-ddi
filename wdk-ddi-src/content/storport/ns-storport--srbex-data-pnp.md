---
UID: NS.storport._SRBEX_DATA_PNP
title: SRBEX_DATA_PNP
author: windows-driver-content
description: The SRBEX_DATA_PNP structure contains the request data for an extended plug and play (PNP) SRB.
old-location: storage\srbex_data_pnp.htm
old-project: storage
ms.assetid: CB64AF68-C40D-44F0-8F52-6BF05E23E5E1
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SRBEX_DATA_PNP, SRBEX_DATA_PNP, *PSRBEX_DATA_PNP
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: storport.h
req.include-header: Storport.h, Srb.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SRBEX_DATA_PNP
req.alt-loc: Storport.h
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

# SRBEX_DATA_PNP structure



## -description
<p>The <b>SRBEX_DATA_PNP</b> structure contains the request data for an extended plug and play (PNP) SRB.</p>


## -syntax

````
typedef struct _SRBEX_DATA_PNP {
  SRBEXDATATYPE   Type;
  ULONG           Length;
  UCHAR           PnPSubFunction;
  UCHAR           Reserved[3];
  STOR_PNP_ACTION PnPAction;
  ULONG           SrbPnPFlags;
  ULONG           Reserved1;
} SRBEX_DATA_PNP, *PSRBEX_DATA_PNP;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>Data type indicator for the bidirectional extended SRB data structure. Set to <b>SrbExDataTypePnp</b>.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>Length of the data in this structure starting with the <b>PnPSubFunction</b> member. Set to SRBEX_DATA_PNP_LENGTH.</p>
</dd>

### -field <b>PnPSubFunction</b>

<dd>
<p>This member is not currently used. Set to 0.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved. Set to 0.</p>
</dd>

### -field <b>PnPAction</b>

<dd>
<p>The plug and play action to perform. This member can have one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="StorStartDevice"></a><a id="storstartdevice"></a><a id="STORSTARTDEVICE"></a><dl>

### -field <b>StorStartDevice</b>


### -field 0x00

</dl>
</td>
<td width="60%">
<p>Start the device.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorRemoveDevice"></a><a id="storremovedevice"></a><a id="STORREMOVEDEVICE"></a><dl>

### -field <b>StorRemoveDevice</b>


### -field 0x02

</dl>
</td>
<td width="60%">
<p>Remove the device.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorStopDevice"></a><a id="storstopdevice"></a><a id="STORSTOPDEVICE"></a><dl>

### -field <b>StorStopDevice</b>


### -field 0x04

</dl>
</td>
<td width="60%">
<p>Stop the device.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorQueryCapabilities"></a><a id="storquerycapabilities"></a><a id="STORQUERYCAPABILITIES"></a><dl>

### -field <b>StorQueryCapabilities</b>


### -field 0x09

</dl>
</td>
<td width="60%">
<p>Query the capabilities of the device.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorQueryResourceRequirements"></a><a id="storqueryresourcerequirements"></a><a id="STORQUERYRESOURCEREQUIREMENTS"></a><dl>

### -field <b>StorQueryResourceRequirements</b>


### -field 0x0B

</dl>
</td>
<td width="60%">
<p>Query the resource requirements for the device.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorFilterResourceRequirements"></a><a id="storfilterresourcerequirements"></a><a id="STORFILTERRESOURCEREQUIREMENTS"></a><dl>

### -field <b>StorFilterResourceRequirements</b>


### -field 0x0D

</dl>
</td>
<td width="60%">
<p>Filter the resource requirements for the device. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorSupriseRemoval"></a><a id="storsupriseremoval"></a><a id="STORSUPRISEREMOVAL"></a><dl>

### -field <b>StorSupriseRemoval</b>


### -field 0x17

</dl>
</td>
<td width="60%">
<p>Surprise Removal of the device. This value is available starting with Windows 7.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>SrbPnPFlags</b>

<dd>
<p>Indicates that the PNP request is for the adapter if SRB_PNP_FLAGS_ADAPTER_REQUEST is set and that storage device address is reserved. Otherwise, <i>SrbPnPFlags</i> will be <b>NULL</b>, indicating that the request is for the storage device specified by an address at <b>AddressOffset</b> in the <a href="..\srb\ns-srb--storage-request-block.md">STORAGE_REQUEST_BLOCK</a> structure.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>This member is reserved. Set to 0.</p>
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
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h or Srb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\srb\ns-srb--storage-request-block.md">STORAGE_REQUEST_BLOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SRBEX_DATA_PNP structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
