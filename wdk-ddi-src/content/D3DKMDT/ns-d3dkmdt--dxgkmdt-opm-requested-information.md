---
UID: NS.d3dkmdt._DXGKMDT_OPM_REQUESTED_INFORMATION
title: DXGKMDT_OPM_REQUESTED_INFORMATION
author: windows-driver-content
description: The DXGKMDT_OPM_REQUESTED_INFORMATION structure contains information that was requested in a call to the DxgkDdiOPMGetInformation or DxgkDdiOPMGetCOPPCompatibleInformation function.
old-location: display\dxgkmdt_opm_requested_information.htm
ms.assetid: c483786a-be8c-4ae3-a48c-45064ce81939
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKMDT_OPM_REQUESTED_INFORMATION
req.alt-loc: d3dkmdt.h
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
ms.keywords: DXGKMDT_OPM_REQUESTED_INFORMATION, DXGKMDT_OPM_REQUESTED_INFORMATION, *PDXGKMDT_OPM_REQUESTED_INFORMATION
req.iface: 
---

# DXGKMDT_OPM_REQUESTED_INFORMATION structure



## -description
<p>The DXGKMDT_OPM_REQUESTED_INFORMATION structure contains information that was requested in a call to the <a href="https://msdn.microsoft.com/3d6559e5-776e-4fc0-b99a-8818cbcc289d">DxgkDdiOPMGetInformation</a> or <a href="https://msdn.microsoft.com/9f15df1e-bdf5-4634-97f1-78515664b594">DxgkDdiOPMGetCOPPCompatibleInformation</a> function.</p>


## -syntax

````
typedef struct _DXGKMDT_OPM_REQUESTED_INFORMATION {
  DXGKMDT_OPM_OMAC omac;
  ULONG            cbRequestedInformationSize;
  BYTE             abRequestedInformation[DXGKMDT_OPM_REQUESTED_INFORMATION_SIZE];
} DXGKMDT_OPM_REQUESTED_INFORMATION, *PDXGKMDT_OPM_REQUESTED_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>omac</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560887">DXGKMDT_OPM_OMAC</a> structure that contains a One-key Cipher Block Chaining (CBC)-mode message authentication code (OMAC) for message authenticity. For more information about OMAC, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=70417">OMAC-1 algorithm</a>. The OMAC-1 parameters that OPM and COPP use are:</p>
<p><i>E</i> = AES (Advanced Encryption Standard)</p>
<p><i>t</i> = 128 bits</p>
<p><i>K</i> = The 128-bit key that the display miniport driver receives when <a href="https://msdn.microsoft.com/285521c7-4034-4db8-9441-6c4eaee27ee3">DxgkDdiOPMSetSigningKeyAndSequenceNumbers</a> is called.</p>
<p><i>n</i> = 128 bits </p>
<p>For information about AES, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=70411">RSA Laboratories</a> website. </p>
</dd>

### -field <b>cbRequestedInformationSize</b>

<dd>
<p>The size, in bytes, of the valid data that the <b>abRequestedInformation</b> member points to. </p>
</dd>

### -field <b>abRequestedInformation</b>

<dd>
<p>A 4076-byte array that specifies the information that is retrieved from a protected output object.</p>
<p>To return the requested information, the display miniport driver should cast <b>abRequestedInformation</b> to one of the following structures, depending on the GUID that was specified in the <b>guidInformation</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560868">DXGKMDT_OPM_GET_INFO_PARAMETERS</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff560859">DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS</a> structure that the <i>Parameters</i> parameter of <a href="https://msdn.microsoft.com/3d6559e5-776e-4fc0-b99a-8818cbcc289d">DxgkDdiOPMGetInformation</a> or <a href="https://msdn.microsoft.com/9f15df1e-bdf5-4634-97f1-78515664b594">DxgkDdiOPMGetCOPPCompatibleInformation</a> points to. As an example, the DXGKMDT_OPM_GET_CONNECTED_HDCP_DEVICE_INFORMATION GUID indicates the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560854">DXGKMDT_OPM_CONNECTED_HDCP_DEVICE_INFORMATION</a> structure.</p>
<table>
<tr>
<th>GUID</th>
<th>Structure for retrieved information</th>
</tr>
<tr>
<td>
<p>
<dl>

### -field DXGKMDT_OPM_GET_CONNECTOR_TYPE, DXGKMDT_OPM_GET_SUPPORTED_PROTECTION_TYPES, DXGKMDT_OPM_GET_VIRTUAL_PROTECTION_LEVEL, DXGKMDT_OPM_GET_ACTUAL_PROTECTION_LEVEL, DXGKMDT_OPM_GET_ADAPTER_BUS_TYPE, 


### -field DXGKMDT_OPM_GET_DVI_CHARACTERISTICS, or DXGKMDT_OPM_GET_CURRENT_HDCP_SRM_VERSION

</dl>
</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560925">DXGKMDT_OPM_STANDARD_INFORMATION</a>
</p>
</td>
</tr>
<tr>
<td>
<p>DXGKMDT_OPM_GET_ACTUAL_OUTPUT_FORMAT</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560840">DXGKMDT_OPM_ACTUAL_OUTPUT_FORMAT</a>
</p>
</td>
</tr>
<tr>
<td>
<p>DXGKMDT_OPM_GET_OUTPUT_ID</p>
</td>
<td>
<p>Supported in Windows 7 and later versions.</p>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560890">DXGKMDT_OPM_OUTPUT_ID</a>
</p>
</td>
</tr>
<tr>
<td>
<p>DXGKMDT_OPM_GET_ACP_AND_CGMSA_SIGNALING</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560830">DXGKMDT_OPM_ACP_AND_CGMSA_SIGNALING</a>
</p>
</td>
</tr>
<tr>
<td>
<p>DXGKMDT_OPM_GET_CONNECTED</p>
<p>_HDCP_DEVICE_INFORMATION</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560854">DXGKMDT_OPM_CONNECTED_HDCP_DEVICE_INFORMATION</a>
</p>
</td>
</tr>
</table>
<p> </p>
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
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/9f15df1e-bdf5-4634-97f1-78515664b594">DxgkDdiOPMGetCOPPCompatibleInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/3d6559e5-776e-4fc0-b99a-8818cbcc289d">DxgkDdiOPMGetInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560830">DXGKMDT_OPM_ACP_AND_CGMSA_SIGNALING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560840">DXGKMDT_OPM_ACTUAL_OUTPUT_FORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560859">DXGKMDT_OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560854">DXGKMDT_OPM_CONNECTED_HDCP_DEVICE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560868">DXGKMDT_OPM_GET_INFO_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560887">DXGKMDT_OPM_OMAC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560890">DXGKMDT_OPM_OUTPUT_ID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560925">DXGKMDT_OPM_STANDARD_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKMDT_OPM_REQUESTED_INFORMATION structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
