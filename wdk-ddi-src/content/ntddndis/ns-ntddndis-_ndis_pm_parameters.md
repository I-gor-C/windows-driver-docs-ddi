---
UID : NS:ntddndis._NDIS_PM_PARAMETERS
title : _NDIS_PM_PARAMETERS
author : windows-driver-content
description : The NDIS_PM_PARAMETERS structure specifies the current or new power management hardware capabilities that are enabled for a network adapter.
old-location : netvista\ndis_pm_parameters.htm
old-project : netvista
ms.assetid : 7747645c-398f-434e-9f0c-21b6d3c7d963
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _NDIS_PM_PARAMETERS, NDIS_PM_PARAMETERS, *PNDIS_PM_PARAMETERS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddndis.h
req.include-header : Ntddndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.20 and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : NDIS_PM_PARAMETERS
req.alt-loc : Ntddndis.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : NDIS_PM_PARAMETERS, *PNDIS_PM_PARAMETERS
---

# _NDIS_PM_PARAMETERS structure
The <b>NDIS_PM_PARAMETERS</b> structure specifies the current or new power management hardware capabilities
  that are enabled for a network adapter.

## Syntax
````
typedef struct _NDIS_PM_PARAMETERS {
  NDIS_OBJECT_HEADER Header;
  ULONG              EnabledWoLPacketPatterns;
  ULONG              EnabledProtocolOffloads;
  ULONG              WakeUpFlags;
#if (NDIS_SUPPORT_NDIS630)
  ULONG              MediaSpecificWakeUpEvents;
#endif 
} NDIS_PM_PARAMETERS, *PNDIS_PM_PARAMETERS;
````

## Members

        
            `EnabledProtocolOffloads`

            A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags that correspond to capabilities that the
     miniport driver reported in the 
     <b>SupportedProtocolOffloads</b> member of the 
     <a href="..\ntddndis\ns-ntddndis-_ndis_pm_capabilities.md">NDIS_PM_CAPABILITIES</a> structure. NDIS
     uses these flags to enable the low power protocol offload capabilities on a network adapter. The
     following flags are used:
        
            `EnabledWoLPacketPatterns`

            A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags that correspond to capabilities that the
     miniport driver reported in the 
     <b>SupportedWoLPacketPatterns</b> member of the 
     <a href="..\ntddndis\ns-ntddndis-_ndis_pm_capabilities.md">NDIS_PM_CAPABILITIES</a> structure. NDIS
     uses these flags to enable the wake-on-LAN (WOL) patterns that a network adapter uses to wake the local
     computer from a low power state. For more information about WOL patterns, see 
     <a href="..\ntddndis\ns-ntddndis-_ndis_pm_wol_pattern.md">NDIS_PM_WOL_PATTERN</a>.
     

The following flags are used:
        
            `Header`

            The type, revision, and size of the <b>NDIS_PM_PARAMETERS</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure.

The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_PM_PARAMETERS</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to the following value:
        
            `MediaSpecificWakeUpEvents`

            A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags. These flags specify the media-specific wake-up events that a network adapter supports. 
     

Starting with NDIS 6.30, the following flags are defined:
        
            `WakeUpFlags`

            A ULONG value that contains a bitwise OR of NDIS_PM_WAKE_ON_
     <i>Xxx</i> flags. NDIS uses these flags to enable wake-up capabilities on
     a network adapter. This member uses the following flags:

    ## Remarks
        The <b>NDIS_PM_PARAMETERS</b> structure specifies the enabled power management hardware capabilities for the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569768">OID_PM_PARAMETERS</a> OID. When the
    OID_PM_PARAMETERS OID is queried, this structure provides the current power management configuration.
    When the OID_PM_PARAMETERS OID is set, this structure specifies a new power management configuration that
    the network adapter should use.

An overlying driver should not try to enable capabilities that a network adapter does not support. To
    enable an overlying driver to determine what capabilities a network adapter provides, NDIS provides the
    capabilities in the 
    <b>PowerManagementCapabilitiesEx</b> member of the 
    <a href="..\ndis\ns-ndis-_ndis_bind_parameters.md">NDIS_BIND_PARAMETERS</a> structure.


<div class="alert"><b>Note</b>  NDIS 6.20 and later drivers must use the 
     <b>PowerManagementCapabilitiesEx</b> member of the 
    <a href="..\ndis\ns-ndis-_ndis_bind_parameters.md">NDIS_BIND_PARAMETERS</a> structure instead of the 
     <b>PowerManagementCapabilities</b> member.</div>
<div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddndis.h (include Ntddndis.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ndis\ns-ndis-_ndis_bind_parameters.md">NDIS_BIND_PARAMETERS</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis-_ndis_pm_capabilities.md">NDIS_PM_CAPABILITIES</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis-_ndis_pm_wol_pattern.md">NDIS_PM_WOL_PATTERN</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/oid-gen-current-packet-filter">OID_GEN_CURRENT_PACKET_FILTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569768">OID_PM_PARAMETERS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PM_PARAMETERS structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>