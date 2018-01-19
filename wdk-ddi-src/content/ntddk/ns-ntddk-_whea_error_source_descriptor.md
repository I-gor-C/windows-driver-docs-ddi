---
UID : NS:ntddk._WHEA_ERROR_SOURCE_DESCRIPTOR
title : _WHEA_ERROR_SOURCE_DESCRIPTOR
author : windows-driver-content
description : The WHEA_ERROR_SOURCE_DESCRIPTOR structure describes an error source.
old-location : whea\whea_error_source_descriptor.htm
old-project : whea
ms.assetid : 59ee6d51-c60a-4a71-b831-1b9437a69d34
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : _WHEA_ERROR_SOURCE_DESCRIPTOR, WHEA_ERROR_SOURCE_DESCRIPTOR, *PWHEA_ERROR_SOURCE_DESCRIPTOR
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddk.h
req.include-header : Ntddk.h
req.target-type : Windows
req.target-min-winverclnt : Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : WHEA_ERROR_SOURCE_DESCRIPTOR
req.alt-loc : ntddk.h
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
req.typenames : WHEA_ERROR_SOURCE_DESCRIPTOR, *PWHEA_ERROR_SOURCE_DESCRIPTOR
---

# _WHEA_ERROR_SOURCE_DESCRIPTOR structure
The WHEA_ERROR_SOURCE_DESCRIPTOR structure describes an error source.

## Syntax
````
typedef struct _WHEA_ERROR_SOURCE_DESCRIPTOR {
  ULONG                   Length;
  ULONG                   Version;
  WHEA_ERROR_SOURCE_TYPE  Type;
  WHEA_ERROR_SOURCE_STATE State;
  ULONG                   MaxRawDataLength;
  ULONG                   NumRecordsToPreallocate;
  ULONG                   MaxSectionsPerRecord;
  ULONG                   ErrorSourceId;
  ULONG                   PlatformErrorSourceId;
  ULONG                   Flags;
  union {
    WHEA_XPF_MCE_DESCRIPTOR       XpfMceDescriptor;
    WHEA_XPF_CMC_DESCRIPTOR       XpfCmcDescriptor;
    WHEA_XPF_NMI_DESCRIPTOR       XpfNmiDescriptor;
    WHEA_IPF_MCA_DESCRIPTOR       IpfMcaDescriptor;
    WHEA_IPF_CMC_DESCRIPTOR       IpfCmcDescriptor;
    WHEA_IPF_CPE_DESCRIPTOR       IpfCpeDescriptor;
    WHEA_AER_ROOTPORT_DESCRIPTOR  AerRootportDescriptor;
    WHEA_AER_ENDPOINT_DESCRIPTOR  AerEndpointDescriptor;
    WHEA_AER_BRIDGE_DESCRIPTOR    AerBridgeDescriptor;
    WHEA_GENERIC_ERROR_DESCRIPTOR GenErrDescriptor;
  } Info;
} WHEA_ERROR_SOURCE_DESCRIPTOR, *PWHEA_ERROR_SOURCE_DESCRIPTOR;
````

## Members

        
            `ErrorSourceId`

            The identifier of the error source. This identifier is unique only on the system where the error source exists.
        
            `Flags`

            A bitwise OR'ed combination of flags that describes the error source. Possible flags are:
        
            `Info`

            A union of descriptor structures that are specific to each different type of error source.
        
            `Length`

            The size, in bytes, of the WHEA_ERROR_SOURCE_DESCRIPTOR structure.
        
            `MaxRawDataLength`

            The maximum number of bytes of raw data included in a hardware error packet that is reported by this error source. This number must be large enough to include any additional platform-specific error information that is added to the hardware error packet by the PSHED or by a PSHED plug-in.
        
            `MaxSectionsPerRecord`

            The maximum number of error record sections that are required in an error record to describe a hardware error that is reported by this error source. This number must be large enough to include any additional error record sections that are added to the error record by the PSHED or by a PSHED plug-in during the processing of the error.
        
            `NumRecordsToPreallocate`

            The number of error records that should be pre-allocated for hardware errors that are reported by this error source.
        
            `PlatformErrorSourceId`

            The identifier of the error source as enumerated by the hardware platform. This identifier is unique only on the system where the error source exists.
        
            `State`

            A <a href="..\ntddk\ne-ntddk-_whea_error_source_state.md">WHEA_ERROR_SOURCE_STATE</a>-typed value that specifies the state of the error source.
        
            `Type`

            A <a href="..\ntddk\ne-ntddk-_whea_error_source_type.md">WHEA_ERROR_SOURCE_TYPE</a>-typed value that specifies the type of the error source.
        
            `Version`

            The version number of the WHEA_ERROR_SOURCE_DESCRIPTOR structure. This member contains the value WHEA_ERROR_SOURCE_DESCRIPTOR_VERSION_10.

    ## Remarks
        The WHEA_ERROR_SOURCE_DESCRIPTOR structure describes an error source. The WHEA_ERROR_SOURCE_DESCRIPTOR structure is also used to configure an error source.

A user-mode WHEA management application can control the error sources in the system by calling the methods in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559521">WHEAErrorSourceMethods</a> WMI provider class.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddk.h (include Ntddk.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ntddk\nc-ntddk-pshed_pi_disable_error_source.md">DisableErrorSource</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pshed_pi_enable_error_source.md">EnableErrorSource</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pshed_pi_get_all_error_sources.md">GetAllErrorSources</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pshed_pi_get_error_source_info.md">GetErrorSourceInfo</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pshed_pi_set_error_source_info.md">SetErrorSourceInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559523">WHEAErrorSourceMethods::DisableErrorSourceRtn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559525">WHEAErrorSourceMethods::EnableErrorSourceRtn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559527">WHEAErrorSourceMethods::GetAllErrorSourcesRtn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559530">WHEAErrorSourceMethods::GetErrorSourceInfoRtn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559531">WHEAErrorSourceMethods::SetErrorSourceInfoRtn</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_aer_bridge_descriptor.md">WHEA_AER_BRIDGE_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_aer_endpoint_descriptor.md">WHEA_AER_ENDPOINT_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_aer_rootport_descriptor.md">WHEA_AER_ROOTPORT_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ntddk\ne-ntddk-_whea_error_source_state.md">WHEA_ERROR_SOURCE_STATE</a>
</dt>
<dt>
<a href="..\ntddk\ne-ntddk-_whea_error_source_type.md">WHEA_ERROR_SOURCE_TYPE</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_generic_error_descriptor.md">WHEA_GENERIC_ERROR_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_ipf_cmc_descriptor.md">WHEA_IPF_CMC_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_ipf_cpe_descriptor.md">WHEA_IPF_CPE_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_ipf_mca_descriptor.md">WHEA_IPF_MCA_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_xpf_cmc_descriptor.md">WHEA_XPF_CMC_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_xpf_mce_descriptor.md">WHEA_XPF_MCE_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_xpf_nmi_descriptor.md">WHEA_XPF_NMI_DESCRIPTOR</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_ERROR_SOURCE_DESCRIPTOR structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>