---
UID: NE.d3dkmddi._DXGK_QUERYADAPTERINFOTYPE
title: DXGK_QUERYADAPTERINFOTYPE
author: windows-driver-content
description: The DXGK_QUERYADAPTERINFOTYPE enumeration indicates the type of information to retrieve.
old-location: display\dxgk_queryadapterinfotype.htm
old-project: display
ms.assetid: 5cceffb1-853c-4635-b855-d0e3f107c23d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_QUERYADAPTERINFOTYPE
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

# DXGK_QUERYADAPTERINFOTYPE enumeration



## -description
<p>The DXGK_QUERYADAPTERINFOTYPE enumeration indicates the type of information to retrieve.</p>


## -syntax

````
typedef enum _DXGK_QUERYADAPTERINFOTYPE { 
  DXGKQAITYPE_UMDRIVERPRIVATE                   = 0,
  DXGKQAITYPE_DRIVERCAPS                        = 1,
  DXGKQAITYPE_QUERYSEGMENT                      = 2,
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN7)
  DXGKQAITYPE_ALLOCATIONGROUP                   = 3,
  DXGKQAITYPE_QUERYSEGMENT2                     = 4,
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
  DXGKQAITYPE_QUERYSEGMENT3                     = 5,
  DXGKQAITYPE_NUMPOWERCOMPONENTS                = 6,
  DXGKQAITYPE_POWERCOMPONENTINFO                = 7,
  DXGKQAITYPE_PREFERREDGPUNODE                  = 8,
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
  DXGKQAITYPE_POWERCOMPONENTPSTATEINFO          = 9,
  DXGKQAITYPE_HISTORYBUFFERPRECISION            = 10,
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
  DXGKQAITYPE_QUERYSEGMENT4                     = 11,
  DXGKQAITYPE_SEGMENTMEMORYSTATE                = 12,
  DXGKQAITYPE_GPUMMUCAPS                        = 13,
  DXGKQAITYPE_PAGETABLELEVELDESC                = 14,
  DXGKQAITYPE_PHYSICALADAPTERCAPS               = 15,
  DXGKQAITYPE_DISPLAY_DRIVERCAPS_EXTENSION      = 16,
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_2)
  DXGKQAITYPE_INTEGRATED_DISPLAY_DESCRIPTOR     = 17,
  DXGKQAITYPE_UEFIFRAMEBUFFERRANGES             = 18,
  DXGKQAITYPE_QUERYCOLORIMETRYOVERRIDES         = 19
} DXGK_QUERYADAPTERINFOTYPE;
````


## -enum-fields
<dl>

### -field <a id="DXGKQAITYPE_UMDRIVERPRIVATE"></a><a id="dxgkqaitype_umdriverprivate"></a><b>DXGKQAITYPE_UMDRIVERPRIVATE</b>

<dd>
<p>Indicates private data for the user-mode display driver.</p>
</dd>

### -field <a id="DXGKQAITYPE_DRIVERCAPS"></a><a id="dxgkqaitype_drivercaps"></a><b>DXGKQAITYPE_DRIVERCAPS</b>

<dd>
<p>Indicates the driver capabilities in a <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-drivercaps.md">DXGK_DRIVERCAPS</a> structure.</p>
</dd>

### -field <a id="DXGKQAITYPE_QUERYSEGMENT"></a><a id="dxgkqaitype_querysegment"></a><b>DXGKQAITYPE_QUERYSEGMENT</b>

<dd>
<p>
      Indicates memory-segment information in a <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-querysegmentout.md">DXGK_QUERYSEGMENTOUT</a> structure.
     </p>
</dd>

### -field <a id="DXGKQAITYPE_ALLOCATIONGROUP"></a><a id="dxgkqaitype_allocationgroup"></a><b>DXGKQAITYPE_ALLOCATIONGROUP</b>

<dd>
<p>
      Reserved for system use. Do not use in your driver. Note that this constant occurs starting with Windows 7.</p>
</dd>

### -field <a id="DXGKQAITYPE_QUERYSEGMENT2"></a><a id="dxgkqaitype_querysegment2"></a><b>DXGKQAITYPE_QUERYSEGMENT2</b>

<dd>
<p>Reserved for system use. Do not use in your driver.
     Note that this constant occurs starting with Windows 7.</p>
</dd>

### -field <a id="DXGKQAITYPE_QUERYSEGMENT3"></a><a id="dxgkqaitype_querysegment3"></a><b>DXGKQAITYPE_QUERYSEGMENT3</b>

<dd>
<p>Indicates memory-segment information in a <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-querysegmentout3.md">DXGK_QUERYSEGMENTOUT3</a> structure.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="DXGKQAITYPE_NUMPOWERCOMPONENTS"></a><a id="dxgkqaitype_numpowercomponents"></a><b>DXGKQAITYPE_NUMPOWERCOMPONENTS</b>

<dd>
<p>Indicates the number of power components used by the display miniport driver.  For more information, see Remarks.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="DXGKQAITYPE_POWERCOMPONENTINFO"></a><a id="dxgkqaitype_powercomponentinfo"></a><b>DXGKQAITYPE_POWERCOMPONENTINFO</b>

<dd>
<p>Indicates information about power components used by the display miniport driver. For more information, see Remarks.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="DXGKQAITYPE_PREFERREDGPUNODE"></a><a id="dxgkqaitype_preferredgpunode"></a><b>DXGKQAITYPE_PREFERREDGPUNODE</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="DXGKQAITYPE_POWERCOMPONENTPSTATEINFO"></a><a id="dxgkqaitype_powercomponentpstateinfo"></a><b>DXGKQAITYPE_POWERCOMPONENTPSTATEINFO</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <a id="DXGKQAITYPE_HISTORYBUFFERPRECISION"></a><a id="dxgkqaitype_historybufferprecision"></a><b>DXGKQAITYPE_HISTORYBUFFERPRECISION</b>

<dd>
<p>Indicates info about the precision of history buffer data used by the display miniport driver. For more information, see Remarks.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <a id="DXGKQAITYPE_QUERYSEGMENT4"></a><a id="dxgkqaitype_querysegment4"></a><b>DXGKQAITYPE_QUERYSEGMENT4</b>

<dd>
<p>Indicates memory-segment information in a <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-querysegmentout4.md">DXGK_QUERYSEGMENTOUT4</a> structure.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <a id="DXGKQAITYPE_SEGMENTMEMORYSTATE"></a><a id="dxgkqaitype_segmentmemorystate"></a><b>DXGKQAITYPE_SEGMENTMEMORYSTATE</b>

<dd>
<p>Indicates bad memory ranges in a <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-memoryrange.md">DXGK_MEMORYRANGE</a> structure. </p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <a id="DXGKQAITYPE_GPUMMUCAPS"></a><a id="dxgkqaitype_gpummucaps"></a><b>DXGKQAITYPE_GPUMMUCAPS</b>

<dd>
<p>Indicates physical adapter GPU capabilities.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <a id="DXGKQAITYPE_PAGETABLELEVELDESC"></a><a id="dxgkqaitype_pagetableleveldesc"></a><b>DXGKQAITYPE_PAGETABLELEVELDESC</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <a id="DXGKQAITYPE_PHYSICALADAPTERCAPS"></a><a id="dxgkqaitype_physicaladaptercaps"></a><b>DXGKQAITYPE_PHYSICALADAPTERCAPS</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <a id="DXGKQAITYPE_DISPLAY_DRIVERCAPS_EXTENSION"></a><a id="dxgkqaitype_display_drivercaps_extension"></a><b>DXGKQAITYPE_DISPLAY_DRIVERCAPS_EXTENSION</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <a id="DXGKQAITYPE_INTEGRATED_DISPLAY_DESCRIPTOR___"></a><a id="dxgkqaitype_integrated_display_descriptor___"></a><b>DXGKQAITYPE_INTEGRATED_DISPLAY_DESCRIPTOR   </b>

<dd>
<p>Indicates a request for an integrated panel descriptor where the input buffer to the query will be a DXGK_QUERYINTEGRATEDDISPLAYIN structure and the output buffer is a DXGK_QUERYINTEGRATEDDISPLAYOUT structure.</p>
<p>Although this function addresses a target, only DxgKrnl adapter locks are taken over this call, not child device locks.  In practice, since this call will be made before the child device is exposed, there should be no concurrent DDI calls which address the same target.</p>
<div class="alert"><b>Note</b>  Unlike most QueryAdapterInfo calls, the output buffer size is variable although it is still known in advance from the DescriptorLength field of the DXGK_INTEGRATED_DISPLAY_CHILD structure for the target id.  The size of the output buffer is:
DescriptorLength + FIELD_OFFSET( DXGK_QUERYINTEGRATEDDISPLAYOUT, Descriptor )
</div>
<div> </div>
</dd>

### -field <a id="DXGKQAITYPE_UEFIFRAMEBUFFERRANGES___________"></a><a id="dxgkqaitype_uefiframebufferranges___________"></a><b>DXGKQAITYPE_UEFIFRAMEBUFFERRANGES           </b>

<dd>
<p>Indicates request for the UEFI frame buffer ranges.</p>
</dd>

### -field <a id="DXGKQAITYPE_QUERYCOLORIMETRYOVERRIDES_______"></a><a id="dxgkqaitype_querycolorimetryoverrides_______"></a><b>DXGKQAITYPE_QUERYCOLORIMETRYOVERRIDES       </b>

<dd>
<p>Indicates a request for colorimetry overrides for an external display where the input buffer to the query will be a DXGK_QUERYCOLORIMETRYOVERRIDESIN structure, containing only the target id being addressed and the output buffer is a DXGK_COLORIMETRY structure into which the driver writes overrides for the monitor attached to the target.</p>
<p>Although this function addresses a target, only DxgKrnl adapter locks are taken over this call, not child device locks.  Since this call will be made before the child device is exposed, there should be no concurrent DDI calls which address the same target.</p>
<p>The output buffer is zeroed when passed to the driver.  If the driver has no overrides for the monitor, it should return STATUS_SUCCESS and leave the output buffer zeroed.  If the driver has overrides, it fill in all fields of the DXGK_COLORIMETRY to describe the monitor capabilities as the OS will not accept partial overrides.</p>
</dd>
</dl>

## -remarks
<p>The display miniport driver must fill the buffer pointed to by the <b>pOutputData</b> member of the <a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-queryadapterinfo.md">DXGKARG_QUERYADAPTERINFO</a> structure as follows:</p>

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
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-power-runtime-component.md">DXGK_POWER_RUNTIME_COMPONENT</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-querysegmentout.md">DXGK_QUERYSEGMENTOUT</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-querysegmentout3.md">DXGK_QUERYSEGMENTOUT3</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-historybufferprecision.md">DXGKARG_HISTORYBUFFERPRECISION</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-queryadapterinfo.md">DXGKARG_QUERYADAPTERINFO</a>
</dt>
<dt>
<a href="display.dxgkddiqueryadapterinfo">DxgkDdiQueryAdapterInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_QUERYADAPTERINFOTYPE enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
