---
UID: NF.ndis.NdisFSetAttributes
title: NdisFSetAttributes
author: windows-driver-content
description: A filter driver calls the NdisFSetAttributes function to specify a filter module context area.
old-location: netvista\ndisfsetattributes.htm
old-project: netvista
ms.assetid: 66e20ac3-e97d-429d-868e-79c04881702b
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NdisFSetAttributes
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisFSetAttributes
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Filter_Driver_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NdisFSetAttributes function



## -description
<p>A filter driver calls the 
  <b>NdisFSetAttributes</b> function to specify a filter module context area.</p>


## -syntax

````
NDIS_STATUS NdisFSetAttributes(
  _In_ NDIS_HANDLE             NdisFilterHandle,
  _In_ NDIS_HANDLE             FilterModuleContext,
  _In_ PNDIS_FILTER_ATTRIBUTES FilterAttributes
);
````


## -parameters
<dl>

### -param NdisFilterHandle [in]

<dd>
<p>The NDIS handle that identifies this filter module. NDIS passed the handle to the filter driver in
     a call to the 
     <a href="..\ndis\nc-ndis-filter-attach.md">FilterAttach</a> function.</p>
</dd>

### -param FilterModuleContext [in]

<dd>
<p>The caller-allocated context area for this filter module.</p>
</dd>

### -param FilterAttributes [in]

<dd>
<p>A pointer to a filter driver allocated 
     <a href="..\ndis\ns-ndis--ndis-filter-attributes.md">
     NDIS_FILTER_ATTRIBUTES</a> structure.</p>
</dd>
</dl>

## -returns
<p><b>NdisFSetAttributes</b> returns one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p><b>NdisFSetAttributes</b> returns NDIS_STATUS_SUCCESS if it set the filter driver attributes.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p><b>NdisFSetAttributes</b> failed because of insufficient resources.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p><b>NdisFSetAttributes</b> returns NDIS_STATUS_FAILURE if none of the preceding values applies.</p>

<p> </p>

## -remarks
<p>A filter driver calls 
    <b>NdisFSetAttributes</b> from its 
    <a href="..\ndis\nc-ndis-filter-attach.md">FilterAttach</a> function and passes the
    handle that NDIS passed to 
    <i>FilterAttach</i> at the 
    <i>NdisFilterHandle</i> parameter. The 
    <i>FilterModuleContext</i> parameter of 
    <b>NdisFSetAttributes</b> specifies the context area for this filter module. NDIS passes the context area
    back to the filter driver in calls to functions such as 
    <a href="..\ndis\nc-ndis-filter-send-net-buffer-lists.md">FilterSendNetBufferLists</a>.</p>

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
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.ndis_irql_filter_driver_function">Irql_Filter_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-filter-attach.md">FilterAttach</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-send-net-buffer-lists.md">FilterSendNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-filter-attributes.md">NDIS_FILTER_ATTRIBUTES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisFSetAttributes function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
