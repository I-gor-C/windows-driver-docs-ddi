---
UID: NS.hidpi._HIDP_CAPS
title: HIDP_CAPS
author: windows-driver-content
description: The HIDP_CAPS structure contains information about a top-level collection's capability.
old-location: hid\hidp_caps.htm
old-project: hid
ms.assetid: ec4d4b7b-acf6-4839-9a61-1883eddce3f4
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HIDP_CAPS, HIDP_CAPS, *PHIDP_CAPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hidpi.h
req.include-header: Hidpi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HIDP_CAPS
req.alt-loc: hidpi.h
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

# HIDP_CAPS structure



## -description
<p>The HIDP_CAPS structure contains information about a top-level <a href="https://msdn.microsoft.com/228fab4f-ff90-43c5-bc68-26b29e8a7dd6">collection's capability</a>.</p>


## -syntax

````
typedef struct _HIDP_CAPS {
  USAGE  Usage;
  USAGE  UsagePage;
  USHORT InputReportByteLength;
  USHORT OutputReportByteLength;
  USHORT FeatureReportByteLength;
  USHORT Reserved[17];
  USHORT NumberLinkCollectionNodes;
  USHORT NumberInputButtonCaps;
  USHORT NumberInputValueCaps;
  USHORT NumberInputDataIndices;
  USHORT NumberOutputButtonCaps;
  USHORT NumberOutputValueCaps;
  USHORT NumberOutputDataIndices;
  USHORT NumberFeatureButtonCaps;
  USHORT NumberFeatureValueCaps;
  USHORT NumberFeatureDataIndices;
} HIDP_CAPS, *PHIDP_CAPS;
````


## -struct-fields
<dl>

### -field <b>Usage</b>

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection's</a> <a href="hid.hid_usages#usage_id#usage_id">usage ID</a>.</p>
</dd>

### -field <b>UsagePage</b>

<dd>
<p>Specifies the top-level collection's <a href="hid.hid_usages#usage_page#usage_page">usage page</a>.</p>
</dd>

### -field <b>InputReportByteLength</b>

<dd>
<p>Specifies the maximum size, in bytes, of all the input reports (including the report ID, if report IDs are used, which is prepended to the report data).</p>
</dd>

### -field <b>OutputReportByteLength</b>

<dd>
<p>Specifies the maximum size, in bytes, of all the output reports (including the report ID, if report IDs are used, which is prepended to the report data).</p>
</dd>

### -field <b>FeatureReportByteLength</b>

<dd>
<p>Specifies the maximum length, in bytes, of all the feature reports (including the report ID, if report IDs are used, which is prepended to the report data).</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for internal system use.</p>
</dd>

### -field <b>NumberLinkCollectionNodes</b>

<dd>
<p>Specifies the number of <a href="..\hidpi\ns-hidpi--hidp-link-collection-node.md">HIDP_LINK_COLLECTION_NODE</a> structures that are returned for this top-level collection by <a href="..\hidpi\nf-hidpi-hidp-getlinkcollectionnodes.md">HidP_GetLinkCollectionNodes</a>.</p>
</dd>

### -field <b>NumberInputButtonCaps</b>

<dd>
<p>Specifies the number of input <a href="..\hidpi\ns-hidpi--hidp-button-caps.md">HIDP_BUTTON_CAPS</a> structures that <a href="..\hidpi\nf-hidpi-hidp-getbuttoncaps.md">HidP_GetButtonCaps</a> returns.</p>
</dd>

### -field <b>NumberInputValueCaps</b>

<dd>
<p>Specifies the number of input <a href="..\hidpi\ns-hidpi--hidp-value-caps.md">HIDP_VALUE_CAPS</a> structures that <a href="..\hidpi\nf-hidpi-hidp-getvaluecaps.md">HidP_GetValueCaps</a> returns.</p>
</dd>

### -field <b>NumberInputDataIndices</b>

<dd>
<p>Specifies the number of <a href="NULL">data indices</a> assigned to buttons and values in all input reports.</p>
</dd>

### -field <b>NumberOutputButtonCaps</b>

<dd>
<p>Specifies the number of output HIDP_BUTTON_CAPS structures that <b>HidP_GetButtonCaps</b> returns.</p>
</dd>

### -field <b>NumberOutputValueCaps</b>

<dd>
<p>Specifies the number of output HIDP_VALUE_CAPS structures that <b>HidP_GetValueCaps</b> returns.</p>
</dd>

### -field <b>NumberOutputDataIndices</b>

<dd>
<p>Specifies the number of data indices assigned to buttons and values in all output reports.</p>
</dd>

### -field <b>NumberFeatureButtonCaps</b>

<dd>
<p>Specifies the total number of feature HIDP_BUTTONS_CAPS structures that <b>HidP_GetButtonCaps</b> returns.</p>
</dd>

### -field <b>NumberFeatureValueCaps</b>

<dd>
<p>Specifies the total number of feature HIDP_VALUE_CAPS structures that <b>HidP_GetValueCaps</b> returns.</p>
</dd>

### -field <b>NumberFeatureDataIndices</b>

<dd>
<p>Specifies the number of data indices assigned to buttons and values in all feature reports.</p>
</dd>
</dl>

## -remarks
<p>Callers of the <a href="hid.hidclass_support_routines">HIDClass support routines</a> use the information provided in this structure when a called routine requires, as input, the size of a report type, the number of link collection nodes, the number of control capabilities, or the number of data indices.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hidpi.h (include Hidpi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getcaps.md">HidP_GetCaps</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getbuttoncaps.md">HidP_GetButtonCaps</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getlinkcollectionnodes.md">HidP_GetLinkCollectionNodes</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getspecificbuttoncaps.md">HidP_GetSpecificButtonCaps</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getspecificvaluecaps.md">HidP_GetSpecificValueCaps</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getvaluecaps.md">HidP_GetValueCaps</a>
</dt>
<dt>
<a href="..\hidpi\ns-hidpi--hidp-link-collection-node.md">HIDP_LINK_COLLECTION_NODE</a>
</dt>
<dt>
<a href="..\hidpi\ns-hidpi--hidp-button-caps.md">HIDP_BUTTON_CAPS</a>
</dt>
<dt>
<a href="..\hidpi\ns-hidpi--hidp-value-caps.md">HIDP_VALUE_CAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HIDP_CAPS structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
