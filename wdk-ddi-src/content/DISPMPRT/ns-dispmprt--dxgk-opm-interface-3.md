---
UID: NS.dispmprt._DXGK_OPM_INTERFACE_3
title: DXGK_OPM_INTERFACE_3
author: windows-driver-content
description: The DXGK_OPM_INTERFACE_3 structure contains pointers to functions in the Output Protection Manager (OPM) Interface, which is implemented by the display miniport driver.
old-location: display\dxgk_opm_interface_3.htm
ms.assetid: 0BD6BA91-7F46-482B-B808-DEB8A23A0B84
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: dispmprt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_OPM_INTERFACE_3
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
req.irql: PASSIVE_LEVEL
ms.keywords: DXGK_OPM_INTERFACE_3, DXGK_OPM_INTERFACE_3, *PDXGK_OPM_INTERFACE_3
req.iface: 
---

# DXGK_OPM_INTERFACE_3 structure



## -description
<p>The DXGK_OPM_INTERFACE_3 structure contains pointers to functions in the <a href="https://msdn.microsoft.com/8dc171f7-76ca-4e1a-865e-7dcb6ab9a2e9">Output Protection Manager (OPM) Interface</a>, which is implemented by the display miniport driver.</p>


## -syntax

````
typedef struct _DXGK_OPM_INTERFACE_3 {
  USHORT                                               Size;
  USHORT                                               Version;
  PVOID                                                Context;
  PINTERFACE_REFERENCE                                 InterfaceReference;
  PINTERFACE_DEREFERENCE                               InterfaceDereference;
  DXGKDDI_OPM_GET_CERTIFICATE_SIZE                     DxgkDdiOPMGetCertificateSize;
  DXGKDDI_OPM_GET_CERTIFICATE                          DxgkDdiOPMGetCertificate;
  DXGKDDI_OPM_CREATE_PROTECTED_OUTPUT                  DxgkDdiOPMCreateProtectedOutput;
  DXGKDDI_OPM_GET_RANDOM_NUMBER                        DxgkDdiOPMGetRandomNumber;
  DXGKDDI_OPM_SET_SIGNING_KEY_AND_SEQUENCE_NUMBERS     DxgkDdiOPMSetSigningKeyAndSequenceNumbers;
  DXGKDDI_OPM_GET_INFORMATION                          DxgkDdiOPMGetInformation;
  DXGKDDI_OPM_GET_COPP_COMPATIBLE_INFORMATION          DxgkDdiOPMGetCOPPCompatibleInformation;
  DXGKDDI_OPM_CONFIGURE_PROTECTED_OUTPUT               DxgkDdiOPMConfigureProtectedOutput;
  DXGKDDI_OPM_DESTROY_PROTECTED_OUTPUT                 DxgkDdiOPMDestroyProtectedOutput;
  DXGKDDI_OPM_CREATE_PROTECTED_OUTPUT_NONLOCAL_DISPLAY DxgkDdiOPMCreateProtectedOutputNonLocalDisplay;
  DXGKDDI_OPM_SET_SRM_LIST                             DxgkDdiOPMSetSrmList;
  DXGKDDI_OPM_GET_SRM_LIST_VERSION                     DxgkDdiOPMGetSrmListVersion;
} DXGK_OPM_INTERFACE_3, *PDXGK_OPM_INTERFACE_3;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>A positive integer that indicates the version number of the OPM interface that is implemented by the display miniport driver. The <b>Version</b> member must be set to DXGK_OPM_INTERFACE_VERSION_1, which is defined in Dispmprt.h.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>A pointer to a private context block. <b>Context</b> must be set to <b>NULL</b>.</p>
</dd>

### -field <b>InterfaceReference</b>

<dd>
<p>A pointer to an interface reference function that is implemented by the display miniport driver. For more information about the operation of an interface reference function, see the Remarks section of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a> structure.</p>
</dd>

### -field <b>InterfaceDereference</b>

<dd>
<p>A pointer to an interface dereference function that is implemented by the display miniport driver. For more information about the operation of an interface dereference function, see the Remarks section of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a> structure.</p>
</dd>

### -field <b>DxgkDdiOPMGetCertificateSize</b>

<dd>
<p>A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/fe4197ad-52a2-47b3-ad96-57ea73cd931f">DxgkDdiOPMGetCertificateSize</a> function.</p>
</dd>

### -field <b>DxgkDdiOPMGetCertificate</b>

<dd>
<p>A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/3c055598-5f07-46e1-830d-1df9a459f742">DxgkDdiOPMGetCertificate</a> function.</p>
</dd>

### -field <b>DxgkDdiOPMCreateProtectedOutput</b>

<dd>
<p>A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/8143732e-cef6-49f1-9b20-db6b6ee073e6">DxgkDdiOPMCreateProtectedOutput</a> function.</p>
</dd>

### -field <b>DxgkDdiOPMGetRandomNumber</b>

<dd>
<p>A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/91b07a5c-ed25-4268-bd6d-273ae8b1ac28">DxgkDdiOPMGetRandomNumber</a> function.</p>
</dd>

### -field <b>DxgkDdiOPMSetSigningKeyAndSequenceNumbers</b>

<dd>
<p>A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/285521c7-4034-4db8-9441-6c4eaee27ee3">DxgkDdiOPMSetSigningKeyAndSequenceNumbers</a> function.</p>
</dd>

### -field <b>DxgkDdiOPMGetInformation</b>

<dd>
<p>A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/3d6559e5-776e-4fc0-b99a-8818cbcc289d">DxgkDdiOPMGetInformation</a> function.</p>
</dd>

### -field <b>DxgkDdiOPMGetCOPPCompatibleInformation</b>

<dd>
<p>A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/9f15df1e-bdf5-4634-97f1-78515664b594">DxgkDdiOPMGetCOPPCompatibleInformation</a> function.</p>
</dd>

### -field <b>DxgkDdiOPMConfigureProtectedOutput</b>

<dd>
<p>A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/a7829587-c1e7-43ec-a0bb-92bca94b7c3d">DxgkDdiOPMConfigureProtectedOutput</a> function.</p>
</dd>

### -field <b>DxgkDdiOPMDestroyProtectedOutput</b>

<dd>
<p>A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/a03381ba-342e-409f-99ab-9790e1d74371">DxgkDdiOPMDestroyProtectedOutput</a> function.</p>
</dd>

### -field <b>DxgkDdiOPMCreateProtectedOutputNonLocalDisplay</b>

<dd>
<p>A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/a03381ba-342e-409f-99ab-9790e1d74371">DxgkDdiOPMCreateProtectedOutputNonLocalDisplay</a> function.</p>
</dd>

### -field <b>DxgkDdiOPMSetSrmList</b>

<dd>
<p>A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/a03381ba-342e-409f-99ab-9790e1d74371">DxgkDdiOPMSetSrmList</a> function.</p>
</dd>

### -field <b>DxgkDdiOPMGetSrmListVersion</b>

<dd>
<p>A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/a03381ba-342e-409f-99ab-9790e1d74371">DxgkDdiOPMGetSrmListVersion</a> function.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h</dt>
</dl>
</td>
</tr>
</table>