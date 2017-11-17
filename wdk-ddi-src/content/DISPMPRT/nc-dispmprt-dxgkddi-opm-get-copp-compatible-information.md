---
UID: NC.dispmprt.DXGKDDI_OPM_GET_COPP_COMPATIBLE_INFORMATION
title: DXGKDDI_OPM_GET_COPP_COMPATIBLE_INFORMATION
author: windows-driver-content
description: The DxgkDdiOPMGetCOPPCompatibleInformation function retrieves information that is compatible with the Certified Output Protection Protocol (COPP) from the given protected output object.
old-location: display\dxgkddiopmgetcoppcompatibleinformation.htm
ms.assetid: 9f15df1e-bdf5-4634-97f1-78515664b594
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkDdiOPMGetCOPPCompatibleInformation
req.alt-loc: dispmprt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
req.iface: IDebugSystemObjects4
---

# DXGKDDI_OPM_GET_COPP_COMPATIBLE_INFORMATION callback



## -description
<p>The<i> DxgkDdiOPMGetCOPPCompatibleInformation</i> function retrieves information that is compatible with the Certified Output Protection Protocol (COPP) from the given protected output object.</p>


## -prototype

````
DXGKDDI_OPM_GET_COPP_COMPATIBLE_INFORMATION DxgkDdiOPMGetCOPPCompatibleInformation;

NTSTATUS DxgkDdiOPMGetCOPPCompatibleInformation(
  _In_        PVOID                                            MiniportDeviceContext,
  _In_        HANDLE                                           ProtectedOutputHandle,
  _In_  const PDXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS Parameters,
  _Out_       PDXGKMDT_OPM_REQUESTED_INFORMATION               RequestedInformation
)
{ ... }
````


## -parameters
<dl>

### -param <i>MiniportDeviceContext</i> [in]

<dd>
<p>A handle to a context block associated with a display adapter. Previously, the display miniport driver's <a href="https://msdn.microsoft.com/5fd4046f-54c3-4dfc-8d51-0d9ebcde0bea">DxgkDdiAddDevice</a> function provided this handle to the DirectX graphics kernel subsystem.</p>
</dd>

### -param <i>ProtectedOutputHandle</i> [in]

<dd>
<p>The handle to a protected output object. The <a href="https://msdn.microsoft.com/8143732e-cef6-49f1-9b20-db6b6ee073e6">DxgkDdiOPMCreateProtectedOutput</a> function creates the protected output object and returns the handle to the object. The protected output object that corresponds to this handle should have COPP semantics.</p>
</dd>

### -param <i>Parameters</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560859">DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS</a> structure that contains the type of COPP-compatible information to retrieve from the protected output object whose handle is specified in the <i>ProtectedOutputHandle</i> parameter. <i>DxgkDdiOPMGetCOPPCompatibleInformation</i> determines if the parameters contain a valid request from the application that indirectly created the protected output object. For more information, see the Remarks section. </p>
</dd>

### -param <i>RequestedInformation</i> [out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560910">DXGKMDT_OPM_REQUESTED_INFORMATION</a> structure that receives the protected output object's COPP-compatible information if <i>DxgkDdiOPMGetCOPPCompatibleInformation</i> returns successfully.</p>
<p>If <i>DxgkDdiOPMGetCOPPCompatibleInformation</i> fails, the value that <i>RequestedInformation</i> points to is unchanged.</p>
</dd>
</dl>

## -returns
<p><i>DxgkDdiOPMGetCOPPCompatibleInformation</i> returns one of the following values.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
<dd>
<p>The function successfully retrieved the protected output object's COPP-compatible information.</p>
</dd>
<dt><b>STATUS_GRAPHICS_OPM_PROTECTED_OUTPUT_DOES_NOT_HAVE_COPP_SEMANTICS</b></dt>
<dd>
<p>The protected output object whose handle is specified in the <i>ProtectedOutputHandle</i> parameter does not have COPP semantics. The DirectX graphics kernel subsystem should call the <a href="https://msdn.microsoft.com/3d6559e5-776e-4fc0-b99a-8818cbcc289d">DxgkDdiOPMGetInformation</a> function instead of <i>DxgkDdiOPMGetCOPPCompatibleInformation </i>for protected output objects with OPM semantics.</p>
</dd>
<dt><b>STATUS_GRAPHICS_OPM_PROTECTED_OUTPUT_DOES_NOT_HAVE_OPM_SEMANTICS</b></dt>
<dd>
<p>OPM-specific information was requested. <i>DxgkDdiOPMGetCOPPCompatibleInformation</i> cannot return OPM-specific information because it can return only COPP-specific information. Callers that require OPM-specific information should create a protected output with OPM semantics and then call <a href="https://msdn.microsoft.com/3d6559e5-776e-4fc0-b99a-8818cbcc289d">DxgkDdiOPMGetInformation</a>. Following are the types of requests (that are specified in the <b>guidInformation</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560859">DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS</a> structure that the <i>Parameters</i> parameter points to) that cause <i>DxgkDdiOPMGetCOPPCompatibleInformation</i> to return this value:</p>
<p></p>
<dl>
<dt><a id="DXGKMDT_OPM_GET_CURRENT_HDCP_SRM_VERSION"></a><a id="dxgkmdt_opm_get_current_hdcp_srm_version"></a>DXGKMDT_OPM_GET_CURRENT_HDCP_SRM_VERSION</dt>
<dd>
<p>Requests the version number of the current High-bandwidth Digital Content Protection (HDCP) System Renewability Message (SRM) for the protected output.</p>
</dd>
<dt><a id="DXGKMDT_OPM_GET_VIRTUAL_PROTECTION_LEVEL_or_DXGKMDT_OPM_GET_ACTUAL_PROTECTION_LEVEL_and_the_first_4_bytes_of_the_abParameters_member_of_DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS_contain_DXGKMDT_OPM_PROTECTION_TYPE_HDCP"></a><a id="dxgkmdt_opm_get_virtual_protection_level_or_dxgkmdt_opm_get_actual_protection_level_and_the_first_4_bytes_of_the_abparameters_member_of_dxgkmdt_opm_copp_compatible_get_info_parameters_contain_dxgkmdt_opm_protection_type_hdcp"></a><a id="DXGKMDT_OPM_GET_VIRTUAL_PROTECTION_LEVEL_OR_DXGKMDT_OPM_GET_ACTUAL_PROTECTION_LEVEL_AND_THE_FIRST_4_BYTES_OF_THE_ABPARAMETERS_MEMBER_OF_DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS_CONTAIN_DXGKMDT_OPM_PROTECTION_TYPE_HDCP"></a>DXGKMDT_OPM_GET_VIRTUAL_PROTECTION_LEVEL or DXGKMDT_OPM_GET_ACTUAL_PROTECTION_LEVEL and the first 4 bytes of the <b>abParameters</b> member of DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS contain DXGKMDT_OPM_PROTECTION_TYPE_HDCP</dt>
<dd>
<p>Requests the virtual or actual HDCP protection level.</p>
</dd>
</dl>
</dd>
<dt><b>STATUS_GRAPHICS_OPM_OUTPUT_DOES_NOT_SUPPORT_HDCP</b></dt>
<dd>
<p>The graphics adapter does not support HDCP. </p>
<p>Following are the types of requests (that are specified in the <b>guidInformation</b> member of DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS) that cause <i>DxgkDdiOPMGetCOPPCompatibleInformation</i> to return this value:</p>
<p></p>
<dl>
<dt><a id="DXGKMDT_OPM_GET_CONNECTED_HDCP_DEVICE_INFORMATION"></a><a id="dxgkmdt_opm_get_connected_hdcp_device_information"></a>DXGKMDT_OPM_GET_CONNECTED_HDCP_DEVICE_INFORMATION</dt>
<dd></dd>
<dt><a id="DXGKMDT_OPM_GET_VIRTUAL_PROTECTION_LEVEL_or_DXGKMDT_OPM_GET_ACTUAL_PROTECTION_LEVEL_and_the_first_4_bytes_of_the_abParameters_member_of_DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS_contain_DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP._"></a><a id="dxgkmdt_opm_get_virtual_protection_level_or_dxgkmdt_opm_get_actual_protection_level_and_the_first_4_bytes_of_the_abparameters_member_of_dxgkmdt_opm_copp_compatible_get_info_parameters_contain_dxgkmdt_opm_protection_type_copp_compatible_hdcp._"></a><a id="DXGKMDT_OPM_GET_VIRTUAL_PROTECTION_LEVEL_OR_DXGKMDT_OPM_GET_ACTUAL_PROTECTION_LEVEL_AND_THE_FIRST_4_BYTES_OF_THE_ABPARAMETERS_MEMBER_OF_DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS_CONTAIN_DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP._"></a>DXGKMDT_OPM_GET_VIRTUAL_PROTECTION_LEVEL or DXGKMDT_OPM_GET_ACTUAL_PROTECTION_LEVEL and the first 4 bytes of the <b>abParameters</b> member of DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS contain DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP. </dt>
<dd></dd>
</dl>
</dd>
<dt><b>STATUS_GRAPHICS_OPM_MONITOR_DOES_NOT_SUPPORT_HDCP</b></dt>
<dd>
<p>The graphics adapter supports High-bandwidth Digital Content Protection (HDCP), but the monitor that is connected to the protected output's physical video output does not support HDCP. For more information about HDCP, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=38728">HDCP Specification Revision 1.1</a>. </p>
<p>Following are the types of requests (that are specified in the <b>guidInformation</b> member of DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS) that cause <i>DxgkDdiOPMGetCOPPCompatibleInformation</i> to return this value:</p>
<p></p>
<dl>
<dt><a id="DXGKMDT_OPM_GET_CONNECTED_HDCP_DEVICE_INFORMATION"></a><a id="dxgkmdt_opm_get_connected_hdcp_device_information"></a>DXGKMDT_OPM_GET_CONNECTED_HDCP_DEVICE_INFORMATION</dt>
<dd></dd>
<dt><a id="DXGKMDT_OPM_GET_VIRTUAL_PROTECTION_LEVEL_or_DXGKMDT_OPM_GET_ACTUAL_PROTECTION_LEVEL_and_the_first_4_bytes_of_the_abParameters_member_of_DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS_contain_DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP._"></a><a id="dxgkmdt_opm_get_virtual_protection_level_or_dxgkmdt_opm_get_actual_protection_level_and_the_first_4_bytes_of_the_abparameters_member_of_dxgkmdt_opm_copp_compatible_get_info_parameters_contain_dxgkmdt_opm_protection_type_copp_compatible_hdcp._"></a><a id="DXGKMDT_OPM_GET_VIRTUAL_PROTECTION_LEVEL_OR_DXGKMDT_OPM_GET_ACTUAL_PROTECTION_LEVEL_AND_THE_FIRST_4_BYTES_OF_THE_ABPARAMETERS_MEMBER_OF_DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS_CONTAIN_DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP._"></a>DXGKMDT_OPM_GET_VIRTUAL_PROTECTION_LEVEL or DXGKMDT_OPM_GET_ACTUAL_PROTECTION_LEVEL and the first 4 bytes of the <b>abParameters</b> member of DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS contain DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP. </dt>
<dd></dd>
</dl>
</dd>
<dt><b>STATUS_GRAPHICS_OPM_OUTPUT_DOES_NOT_SUPPORT_ACP</b></dt>
<dd>
<p>The protected output object whose handle is specified in the <i>ProtectedOutputHandle</i> parameter does not support Analog Copy Protection (ACP), the <b>guidInformation</b> member of DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS specifies DXGKMDT_OPM_GET_VIRTUAL_PROTECTION_LEVEL or DXGKMDT_OPM_GET_ACTUAL_PROTECTION_LEVEL, and the first 4 bytes of the <b>abParameters</b> member of DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS contain DXGKMDT_OPM_PROTECTION_TYPE_ACP. ACP protects analog TV signals. For more information about ACP, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=71273">Rovi (formerly Macrovision)</a> website.</p>
</dd>
<dt><b>STATUS_GRAPHICS_OPM_OUTPUT_DOES_NOT_SUPPORT_CGMSA</b></dt>
<dd>
<p>The protected output object whose handle is specified in the <i>ProtectedOutputHandle</i> parameter does not support Content Generation Management System Analog (CGMS-A) and redistributable control, the <b>guidInformation</b> member of DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS specifies DXGKMDT_OPM_GET_VIRTUAL_PROTECTION_LEVEL or DXGKMDT_OPM_GET_ACTUAL_PROTECTION_LEVEL, and the first 4 bytes of the <b>abParameters</b> member of DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS contain DXGKMDT_OPM_PROTECTION_TYPE_CGMSA. CGMS-A protects analog TV signals. For more information about CGMS-A, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=70568">CGMS-A article</a>. </p>
</dd>
<dt><b>STATUS_GRAPHICS_OPM_SIGNALING_NOT_SUPPORTED</b></dt>
<dd>
<p>The <b>guidInformation</b> member of DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS specifies DXGKMDT_OPM_GET_ACP_AND_CGMSA_SIGNALING and the protected output does not support ACP and CGMS-A. This error code should also be returned if the driver does not support DXGKMDT_OPM_GET_ACP_AND_CGMSA_SIGNALING. Drivers are not required to support DXGKMDT_OPM_GET_ACP_AND_CGMSA_SIGNALING. </p>
</dd>
<dt><b>STATUS_GRAPHICS_OPM_INVALID_INFORMATION_REQUEST</b></dt>
<dd>
<p>The <b>ulSequenceNumber</b> member of DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS contains an invalid sequence number. </p>
</dd>
</dl><p>The function successfully retrieved the protected output object's COPP-compatible information.</p>

<p>The protected output object whose handle is specified in the <i>ProtectedOutputHandle</i> parameter does not have COPP semantics. The DirectX graphics kernel subsystem should call the <a href="https://msdn.microsoft.com/3d6559e5-776e-4fc0-b99a-8818cbcc289d">DxgkDdiOPMGetInformation</a> function instead of <i>DxgkDdiOPMGetCOPPCompatibleInformation </i>for protected output objects with OPM semantics.</p>

<p>OPM-specific information was requested. <i>DxgkDdiOPMGetCOPPCompatibleInformation</i> cannot return OPM-specific information because it can return only COPP-specific information. Callers that require OPM-specific information should create a protected output with OPM semantics and then call <a href="https://msdn.microsoft.com/3d6559e5-776e-4fc0-b99a-8818cbcc289d">DxgkDdiOPMGetInformation</a>. Following are the types of requests (that are specified in the <b>guidInformation</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560859">DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS</a> structure that the <i>Parameters</i> parameter points to) that cause <i>DxgkDdiOPMGetCOPPCompatibleInformation</i> to return this value:</p>

## -remarks
<p>The DirectX graphics kernel subsystem should call <i>DxgkDdiOPMGetCOPPCompatibleInformation</i> only if the output has COPP semantics.</p>

<p>Before the DirectX graphics kernel subsystem passes the protected output handle to the <i>ProtectedOutputHandle</i> parameter in a call to <i>DxgkDdiOPMGetCOPPCompatibleInformation</i>, the DirectX graphics kernel subsystem always passes the protected output handle to the <a href="https://msdn.microsoft.com/285521c7-4034-4db8-9441-6c4eaee27ee3">DxgkDdiOPMSetSigningKeyAndSequenceNumbers</a> and <a href="https://msdn.microsoft.com/91b07a5c-ed25-4268-bd6d-273ae8b1ac28">DxgkDdiOPMGetRandomNumber</a> functions. </p>

<p>Following are some facts that pertain to <i>DxgkDdiOPMGetCOPPCompatibleInformation</i> and that do not pertain to the <a href="https://msdn.microsoft.com/3d6559e5-776e-4fc0-b99a-8818cbcc289d">DxgkDdiOPMGetInformation</a> function:</p>

<p>The DirectX graphics kernel subsystem can pass a handle to a protected output only with COPP semantics. </p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560859">DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS</a> structure that the <i>Parameters</i> parameter points to is not signed.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/5fd4046f-54c3-4dfc-8d51-0d9ebcde0bea">DxgkDdiAddDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a7829587-c1e7-43ec-a0bb-92bca94b7c3d">DxgkDdiOPMConfigureProtectedOutput</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8143732e-cef6-49f1-9b20-db6b6ee073e6">DxgkDdiOPMCreateProtectedOutput</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/91b07a5c-ed25-4268-bd6d-273ae8b1ac28">DxgkDdiOPMGetRandomNumber</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/285521c7-4034-4db8-9441-6c4eaee27ee3">DxgkDdiOPMSetSigningKeyAndSequenceNumbers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560859">DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560887">DXGKMDT_OPM_OMAC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560910">DXGKMDT_OPM_REQUESTED_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_OPM_GET_COPP_COMPATIBLE_INFORMATION callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
