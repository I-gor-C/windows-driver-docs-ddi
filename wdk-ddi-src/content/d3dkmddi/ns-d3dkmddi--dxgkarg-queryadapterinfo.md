---
UID: NS.d3dkmddi._DXGKARG_QUERYADAPTERINFO
title: DXGKARG_QUERYADAPTERINFO
author: windows-driver-content
description: The DXGKARG_QUERYADAPTERINFO structure contains parameters for a query.
old-location: display\dxgkarg_queryadapterinfo.htm
old-project: display
ms.assetid: 5992c846-93de-4f95-839a-81f14db709f7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_QUERYADAPTERINFO, DXGKARG_QUERYADAPTERINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_QUERYADAPTERINFO
req.alt-loc: d3dkmddi.h
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

# DXGKARG_QUERYADAPTERINFO structure



## -description
<p>The DXGKARG_QUERYADAPTERINFO structure contains parameters for a query.</p>


## -syntax

````
typedef struct _DXGKARG_QUERYADAPTERINFO {
  DXGK_QUERYADAPTERINFOTYPE Type;
  VOID                      *pInputData;
  UINT                      InputDataSize;
  VOID                      *pOutputData;
  UINT                      OutputDataSize;
} DXGKARG_QUERYADAPTERINFO;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>[in] A <a href="..\d3dkmddi\ne-d3dkmddi--dxgk-queryadapterinfotype.md">DXGK_QUERYADAPTERINFOTYPE</a>-typed value that indicates the type of information to retrieve.</p>
</dd>

### -field <b>pInputData</b>

<dd>
<p>[in] A pointer to input information for the query. </p>
<p>When <b>Type</b> specifies DXGKQAITYPE_UMDRIVERPRIVATE, <b>pInputData</b> points to a proprietary buffer that contains information about the query. When <b>Type</b> specifies DXGKQAITYPE_QUERYSEGMENT, <b>pInputData</b> points to a <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-querysegmentin.md">DXGK_QUERYSEGMENTIN</a> structure. When <b>Type</b> specifies <b>DXGKQAITYPE_POWERCOMPONENTINFO</b>, <b>pInputData</b> points to an input buffer that contains the power component index.</p>
<p>An input buffer is not required when <b>Type</b> specifies the DXGKQAITYPE_DRIVERCAPS value.</p>
</dd>

### -field <b>InputDataSize</b>

<dd>
<p>[in] The size, in bytes, of the input data that <b>pInputData</b> points to.</p>
</dd>

### -field <b>pOutputData</b>

<dd>
<p>[out] A pointer to an output buffer that the display miniport driver fills with the required information.</p>
<table>
<tr>
<th>Value of <b>Type</b></th>
<th>Contents of output buffer pointed to by <b>pOutputData</b></th>
</tr>
<tr>
<td><b>DXGKQAITYPE_UMDRIVERPRIVATE</b></td>
<td>Proprietary buffer</td>
</tr>
<tr>
<td><b>DXGKQAITYPE_DRIVERCAPS</b></td>
<td>Populated <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-drivercaps.md">DXGK_DRIVERCAPS</a> structure</td>
</tr>
<tr>
<td><b>DXGKQAITYPE_QUERYSEGMENT</b></td>
<td>Populated <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-querysegmentout.md">DXGK_QUERYSEGMENTOUT</a> structure</td>
</tr>
<tr>
<td><b>DXGKQAITYPE_QUERYSEGMENT3</b></td>
<td>Populated <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-querysegmentout3.md">DXGK_QUERYSEGMENTOUT3</a> structure</td>
</tr>
<tr>
<td><b>DXGKQAITYPE_NUMPOWERCOMPONENTS</b></td>
<td>A UINT value that specifies the number of power components used by the display miniport driver</td>
</tr>
<tr>
<td><b>DXGKQAITYPE_POWERCOMPONENTINFO</b></td>
<td>Populated <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-power-runtime-component.md">DXGK_POWER_RUNTIME_COMPONENT</a> structure that provides information about the <i>n</i>th power component, where <i>n</i> is the component index specified by  <b>pInputData</b> in a call to the <a href="display.dxgkddiqueryadapterinfo">DxgkDdiQueryAdapterInfo</a> function</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>OutputDataSize</b>

<dd>
<p>[in] The size, in bytes, of the output data that <b>pOutputData</b> points to.</p>
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
<p>Available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-drivercaps.md">DXGK_DRIVERCAPS</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-power-p-component.md">DXGK_POWER_P_COMPONENT</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-power-runtime-component.md">DXGK_POWER_RUNTIME_COMPONENT</a>
</dt>
<dt>
<a href="..\d3dkmddi\ne-d3dkmddi--dxgk-queryadapterinfotype.md">DXGK_QUERYADAPTERINFOTYPE</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-querysegmentin.md">DXGK_QUERYSEGMENTIN</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-querysegmentout.md">DXGK_QUERYSEGMENTOUT</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-querysegmentout3.md">DXGK_QUERYSEGMENTOUT3</a>
</dt>
<dt>
<a href="display.dxgkddiqueryadapterinfo">DxgkDdiQueryAdapterInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_QUERYADAPTERINFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
