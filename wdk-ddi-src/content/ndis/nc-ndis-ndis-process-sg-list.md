---
UID: NC.ndis.NDIS_PROCESS_SG_LIST
title: NDIS_PROCESS_SG_LIST
author: windows-driver-content
description: The NetProcessSGList function (NDIS_PROCESS_SG_LIST_HANDLER entry point) processes a scatter/gather list.
old-location: netvista\netprocesssglist.htm
old-project: netvista
ms.assetid: 5b99e0ec-7c82-46d6-b32a-246b368cf4f1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NetProcessSGList
req.alt-loc: Ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: = DISPATCH_LEVEL
req.iface: 
---

# NDIS_PROCESS_SG_LIST callback



## -description
<p>The 
  <i>NetProcessSGList</i> function (NDIS_PROCESS_SG_LIST_HANDLER entry point) processes a scatter/gather
  list.</p>


## -prototype

````
NDIS_PROCESS_SG_LIST NetProcessSGList;

VOID NetProcessSGList(
  _In_ PDEVICE_OBJECT       DeviceObject,
  _In_ PVOID                Reserved,
  _In_ PSCATTER_GATHER_LIST ScatterGatherListBuffer,
  _In_ PVOID                Context
)
{ ... }
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>A pointer to a 
     <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a> structure.</p>
</dd>

### -param <i>Reserved</i> [in]

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -param <i>ScatterGatherListBuffer</i> [in]

<dd>
<p>A pointer to a 
     <a href="..\wdm\ns-wdm--scatter-gather-list.md">SCATTER_GATHER_LIST</a> structure.</p>
</dd>

### -param <i>Context</i> [in]

<dd>
<p>A pointer to a block of driver-allocated context information that contains information about the
     scatter gather list. The driver provided this context information in the 
     <b>Context</b> member of the 
     <a href="..\ndis\ns-ndis--ndis-scatter-gather-list-parameters.md">
     NDIS_SCATTER_GATHER_LIST_PARAMETERS</a> structure.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>NDIS calls the 
    <i>NetProcessSGList</i> function that is specified at the 
    <b>ProcessSGListHandler</b> member of the 
    <a href="..\ndis\ns-ndis--ndis-scatter-gather-list-parameters.md">
    NDIS_SCATTER_GATHER_LIST_PARAMETERS</a> structure within the context of the 
    <a href="..\ndis\nf-ndis-ndisbuildscattergatherlist.md">
    NdisBuildScatterGatherList</a> function.</p>

<p>The driver specified the entry point (NDIS_PROCESS_SG_LIST_HANDLER) for 
    <i>NetProcessSGList</i> in the NDIS_SCATTER_GATHER_LIST_PARAMETERS structure.</p>

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
<p>Supported in NDIS 6.20 and later.</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-scatter-gather-list-parameters.md">
   NDIS_SCATTER_GATHER_LIST_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisbuildscattergatherlist.md">NdisBuildScatterGatherList</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--scatter-gather-list.md">SCATTER_GATHER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PROCESS_SG_LIST callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
