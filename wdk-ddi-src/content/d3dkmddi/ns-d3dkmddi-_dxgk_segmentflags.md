---
UID: NS:d3dkmddi._DXGK_SEGMENTFLAGS
title: "_DXGK_SEGMENTFLAGS"
author: windows-driver-content
description: The DXGK_SEGMENTFLAGS structure identifies properties for a segment that the driver provides through a call to its DxgkDdiQueryAdapterInfo function.
old-location: display\dxgk_segmentflags.htm
old-project: display
ms.assetid: 959dfdb2-cadf-427d-958a-33ce2a1610ae
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_SEGMENTFLAGS, DXGK_SEGMENTFLAGS structure [Display Devices], DmStructs_a7239928-eb4e-42d0-8ced-9e37d28e9464.xml, _DXGK_SEGMENTFLAGS, d3dkmddi/DXGK_SEGMENTFLAGS, display.dxgk_segmentflags
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_SEGMENTFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_SEGMENTFLAGS
---

# _DXGK_SEGMENTFLAGS structure
The DXGK_SEGMENTFLAGS structure identifies properties for a segment that the driver provides through a call to its <a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a> function.

## Syntax
```
typedef struct _DXGK_SEGMENTFLAGS {
  union {
    struct {
      UINT  : 1  Aperture;
      UINT  : 1  Agp;
      UINT  : 1  CpuVisible;
      UINT  : 1  UseBanking;
      UINT  : 1  CacheCoherent;
      UINT  : 1  PitchAlignment;
      UINT  : 1  PopulatedFromSystemMemory;
      UINT  : 1  PreservedDuringStandby;
      UINT  : 1  PreservedDuringHibernate;
      UINT  : 1  PartiallyPreservedDuringHibernate;
      UINT  : 1  DirectFlip;
      UINT  : 1  Use64KBPages;
      UINT  : 1  ReservedSysMem;
      UINT  : 1  SupportsCpuHostAperture;
      UINT  : 1  SupportsCachedCpuHostAperture;
      UINT  : 1  ApplicationTarget;
      UINT  : 1  VprSupported;
      UINT  : 1  VprPreservedDuringStandby;
      UINT  : 1  EncryptedPagingSupported;
      UINT  : 1  LocalBudgetGroup;
      UINT  : 1  NonLocalBudgetGroup;
#if ...
      UINT  : 11 Reserved;
#elif
      UINT  : 21 Reserved;
#else
      UINT  : 22 Reserved;
#endif
    };
    UINT Value;
  };
} DXGK_SEGMENTFLAGS;
```

## Members


## Remarks
The driver can specify properties of the segment by setting bits in the 32-bit <b>Value</b> member or by setting individual members of the structure in the union that DXGK_SEGMENTFLAGS contains.

Note that for an AGP-type aperture segment, the driver must exclusively set the <b>Agp</b> member of the structure in the union that DXGK_SEGMENTFLAGS contains. Although the AGP-type aperture segment is an aperture and visible to the CPU, if any other members are set, the adapter fails to initialize.

In the special case where the allocation uses an aperture segment on a shared primary allocation (<a href="https://msdn.microsoft.com/library/windows/hardware/ff557598">DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA</a>.<b>StandardAllocationType</b> is <b>D3DKMDT_STANDARDALLOCATION_SHAREDPRIMARYSURFACE</b>), and <a href="https://msdn.microsoft.com/library/windows/hardware/ff560966">DXGK_ALLOCATIONINFOFLAGS</a>.<b>UseAlternateVA</b> is not set,  the driver should use a section-backed primary allocation (<a href="https://msdn.microsoft.com/library/windows/hardware/ff562072">DXGK_VIDMMCAPS</a>.<b>SectionBackedPrimary</b> is set) when the driver's <a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a> function is called. By using a section-backed primary you can avoid the limitations of <b>CpuVisible</b> for the aperture segment.

You can avoid the limitations of <b>CpuVisible</b> for an aperture segment by using a shared, section-backed primary allocation. In this case, use an aperture segment on a shared primary allocation (<a href="https://msdn.microsoft.com/library/windows/hardware/ff557598">DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA</a>.<b>StandardAllocationType</b> is <b>D3DKMDT_STANDARDALLOCATION_SHAREDPRIMARYSURFACE</b>), do not set <a href="https://msdn.microsoft.com/library/windows/hardware/ff560966">DXGK_ALLOCATIONINFOFLAGS</a>.<b>UseAlternateVA</b>,  and use a section-backed primary allocation (set <a href="https://msdn.microsoft.com/library/windows/hardware/ff562072">DXGK_VIDMMCAPS</a>.<b>SectionBackedPrimary</b>) when the driver's <a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a> function is called. 

<h3><a id="optimized_standby_settings"></a><a id="OPTIMIZED_STANDBY_SETTINGS"></a>Optimized standby settings</h3>
The combination of values for the <b>PreservedDuringStandby</b>, <b>PreservedDuringHibernate</b>, and  <b>PartiallyPreservedDuringHibernate</b> members determines whether a segment is purged of its content when the system enters a low-power (standby) system state, as follows.

<table>
<tr>
<th>Preserved During Standby</th>
<th>Preserved During Hibernate</th>
<th>Partially Preserved During Hibernate</th>
<th>Standby State</th>
<th>Hibernate State</th>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>1</td>
<td>invalid</td>
<td>invalid</td>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>0</td>
<td>not purged</td>
<td>not purged</td>
</tr>
<tr>
<td>1</td>
<td>0</td>
<td>1</td>
<td>not purged</td>
<td>partially purged</td>
</tr>
<tr>
<td>1</td>
<td>0</td>
<td>0</td>
<td>not purged</td>
<td>purged</td>
</tr>
<tr>
<td>0</td>
<td>1</td>
<td>1</td>
<td>invalid</td>
<td>invalid</td>
</tr>
<tr>
<td>0</td>
<td>1</td>
<td>0</td>
<td>invalid</td>
<td>invalid</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>1</td>
<td>invalid</td>
<td>invalid</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>0</td>
<td>purged</td>
<td>purged</td>
</tr>
</table>
 

The operating system does not recognize combinations in this table that are marked "invalid."

If the <a href="https://msdn.microsoft.com/library/windows/hardware/mt608297">hybrid sleep</a> mode is enabled, the system acts as if it is hibernating: it purges segments that are not preserved during hibernate, even if it is going into a low-power state.


The following are common combinations of member values.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows Vista. Available starting with Windows Vista. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557621">DXGKARG_QUERYADAPTERINFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560960">DXGK_ALLOCATIONINFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562015">DXGK_QUERYSEGMENTIN</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562035">DXGK_SEGMENTDESCRIPTOR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh464086">DXGK_SEGMENTDESCRIPTOR3</a>



<a href="https://msdn.microsoft.com/d315ff53-4a9f-46a3-ad74-d65a5eb72de1">DxgkDdiBuildPagingBuffer</a>



<a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a>