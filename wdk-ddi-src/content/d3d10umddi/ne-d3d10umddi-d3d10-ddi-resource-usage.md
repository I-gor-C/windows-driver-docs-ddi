---
UID: NE.d3d10umddi.D3D10_DDI_RESOURCE_USAGE
title: D3D10_DDI_RESOURCE_USAGE
author: windows-driver-content
description: The D3D10_DDI_RESOURCE_USAGE enumeration type contains values that identify how a resource is used.
old-location: display\d3d10_ddi_resource_usage.htm
old-project: display
ms.assetid: f412b665-3489-4200-8fb8-7b6eb564ba98
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10_DDI_RESOURCE_USAGE
req.alt-loc: d3d10umddi.h
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
---

# D3D10_DDI_RESOURCE_USAGE enumeration



## -description
<p>The D3D10_DDI_RESOURCE_USAGE enumeration type contains values that identify how a resource is used.</p>


## -syntax

````
typedef enum D3D10_DDI_RESOURCE_USAGE { 
  D3D10_DDI_USAGE_DEFAULT    = 0,
  D3D10_DDI_USAGE_IMMUTABLE  = 1,
  D3D10_DDI_USAGE_DYNAMIC    = 2,
  D3D10_DDI_USAGE_STAGING    = 3
} D3D10_DDI_RESOURCE_USAGE;
````


## -enum-fields
<dl>

### -field <a id="D3D10_DDI_USAGE_DEFAULT"></a><a id="d3d10_ddi_usage_default"></a><b>D3D10_DDI_USAGE_DEFAULT</b>

<dd>
<p>The resource is used at the highest level. An application cannot map to default resources. The resources can be bound to the graphics pipeline and used as copy destinations and sources. The Microsoft Direct3D runtime can call only the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceupdatesubresourceup.md">ResourceUpdateSubresourceUP</a> function to update the contents directly with the CPU.</p>
</dd>

### -field <a id="D3D10_DDI_USAGE_IMMUTABLE"></a><a id="d3d10_ddi_usage_immutable"></a><b>D3D10_DDI_USAGE_IMMUTABLE</b>

<dd>
<p>The resource is immutable and cannot be mapped or copied to. The resource can be bound to the pipeline and copied from. The Direct3D runtime cannot call <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceupdatesubresourceup.md">ResourceUpdateSubresourceUP</a> to update the contents; therefore, the contents of the resource are provided at creation time.</p>
</dd>

### -field <a id="D3D10_DDI_USAGE_DYNAMIC"></a><a id="d3d10_ddi_usage_dynamic"></a><b>D3D10_DDI_USAGE_DYNAMIC</b>

<dd>
<p>The resource is dynamic and should be resident in non-local video memory. The resource can also be mapped. However, when the resource is mapped, the CPU can only write (and not read) to the resource. Therefore, when mapped, the Direct3D runtime must use the D3D10_DDI_MAP_WRITE_DISCARD or D3D10_DDI_MAP_WRITE_NOOVERWRITE access level in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a> function. Because this resource can be mapped, the runtime cannot call <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceupdatesubresourceup.md">ResourceUpdateSubresourceUP</a>. </p>
</dd>

### -field <a id="D3D10_DDI_USAGE_STAGING"></a><a id="d3d10_ddi_usage_staging"></a><b>D3D10_DDI_USAGE_STAGING</b>

<dd>
<p>The resource is a staging resource, which the user-mode display driver should allocate as system memory. The driver allocates system memory to ensure the proper alignment and pitch to enable DMA access to such a region of memory. Staging can be mapped by the application but cannot be bound to the 3-D graphics pipeline. However, staging resources are frequently used to copy between other non-mappable resources. Because this resource can be mapped, the runtime cannot call <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceupdatesubresourceup.md">ResourceUpdateSubresourceUP</a>. </p>
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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-createresource.md">D3D10DDIARG_CREATERESOURCE</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcemap.md">ResourceMap</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourceupdatesubresourceup.md">ResourceUpdateSubresourceUP</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10_DDI_RESOURCE_USAGE enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
