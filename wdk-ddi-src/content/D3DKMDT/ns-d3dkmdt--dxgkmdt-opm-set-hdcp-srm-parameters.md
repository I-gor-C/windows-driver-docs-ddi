---
UID: NS.d3dkmdt._DXGKMDT_OPM_SET_HDCP_SRM_PARAMETERS
title: DXGKMDT_OPM_SET_HDCP_SRM_PARAMETERS
author: windows-driver-content
description: The DXGKMDT_OPM_SET_HDCP_SRM_PARAMETERS structure contains parameters to set the version of a High-bandwidth Digital Content Protection (HDCP) System Renewability Message (SRM) for a protected output.
old-location: display\dxgkmdt_opm_set_hdcp_srm_parameters.htm
ms.assetid: fd069b0c-9af3-4442-aba0-1d81465e7eb0
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
req.alt-api: DXGKMDT_OPM_SET_HDCP_SRM_PARAMETERS
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
ms.keywords: DXGKMDT_OPM_SET_HDCP_SRM_PARAMETERS, DXGKMDT_OPM_SET_HDCP_SRM_PARAMETERS
req.iface: 
---

# DXGKMDT_OPM_SET_HDCP_SRM_PARAMETERS structure



## -description
<p>The DXGKMDT_OPM_SET_HDCP_SRM_PARAMETERS structure contains parameters to set the version of a High-bandwidth Digital Content Protection (HDCP) System Renewability Message (SRM) for a protected output.</p>


## -syntax

````
typedef struct _DXGKMDT_OPM_SET_HDCP_SRM_PARAMETERS {
  ULONG ulSRMVersion;
} DXGKMDT_OPM_SET_HDCP_SRM_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>ulSRMVersion</b>

<dd>
<p>The version number of an HDCP SRM. The least significant bits (bits 0 through 15) contain the SRM's version number in little-endian format. The SRM's version number is stored in the SRM's SRM version field in little-endian format. For more information about the SRM's SRM version field, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=38728">HDCP Specification Revision 1.1</a>. </p>
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
<a href="https://msdn.microsoft.com/a7829587-c1e7-43ec-a0bb-92bca94b7c3d">DxgkDdiOPMConfigureProtectedOutput</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560849">DXGKMDT_OPM_CONFIGURE_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKMDT_OPM_SET_HDCP_SRM_PARAMETERS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
