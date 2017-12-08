---
UID: NS.dispmprt._DXGK_OPM_INTERFACE
title: DXGK_OPM_INTERFACE
author: windows-driver-content
description: The DXGK_OPM_INTERFACE structure contains pointers to functions in the Output Protection Manager (OPM) Interface, which is implemented by the display miniport driver.
old-location: display\dxgk_opm_interface.htm
old-project: display
ms.assetid: 6ae1d9a8-db9a-460d-b258-222a2bd96265
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_OPM_INTERFACE, DXGK_OPM_INTERFACE, *PDXGK_OPM_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_OPM_INTERFACE
req.alt-loc: Dispmprt.h
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

# DXGK_OPM_INTERFACE structure



## -description
<p>The DXGK_OPM_INTERFACE structure contains pointers to functions in the <a href="display.opm_interface">Output Protection Manager (OPM) Interface</a>, which is implemented by the display miniport driver.</p>


## -syntax

````
typedef struct _DXGK_OPM_INTERFACE {
  USHORT                                           Size;
  USHORT                                           Version;
  PVOID                                            Context;
  PINTERFACE_REFERENCE                             InterfaceReference;
  PINTERFACE_DEREFERENCE                           InterfaceDereference;
  DXGKDDI_OPM_GET_CERTIFICATE_SIZE                 DxgkDdiOPMGetCertificateSize;
  DXGKDDI_OPM_GET_CERTIFICATE                      DxgkDdiOPMGetCertificate;
  DXGKDDI_OPM_CREATE_PROTECTED_OUTPUT              DxgkDdiOPMCreateProtectedOutput;
  DXGKDDI_OPM_GET_RANDOM_NUMBER                    DxgkDdiOPMGetRandomNumber;
  DXGKDDI_OPM_SET_SIGNING_KEY_AND_SEQUENCE_NUMBERS DxgkDdiOPMSetSigningKeyAndSequenceNumbers;
  DXGKDDI_OPM_GET_INFORMATION                      DxgkDdiOPMGetInformation;
  DXGKDDI_OPM_GET_COPP_COMPATIBLE_INFORMATION      DxgkDdiOPMGetCOPPCompatibleInformation;
  DXGKDDI_OPM_CONFIGURE_PROTECTED_OUTPUT           DxgkDdiOPMConfigureProtectedOutput;
  DXGKDDI_OPM_DESTROY_PROTECTED_OUTPUT             DxgkDdiOPMDestroyProtectedOutput;
} DXGK_OPM_INTERFACE, *PDXGK_OPM_INTERFACE;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field Version

<dd>
<p>A positive integer that indicates the version number of the OPM interface that is implemented by the display miniport driver. The <b>Version</b> member must be set to DXGK_OPM_INTERFACE_VERSION_1, which is defined in Dispmprt.h.</p>
</dd>

### -field Context

<dd>
<p>A pointer to a private context block. <b>Context</b> must be set to <b>NULL</b>.</p>
</dd>

### -field InterfaceReference

<dd>
<p>A pointer to an interface reference function that is implemented by the display miniport driver. For more information about the operation of an interface reference function, see the Remarks section of the <a href="..\wdm\ns-wdm--interface.md">INTERFACE</a> structure.</p>
</dd>

### -field InterfaceDereference

<dd>
<p>A pointer to an interface dereference function that is implemented by the display miniport driver. For more information about the operation of an interface dereference function, see the Remarks section of the <a href="..\wdm\ns-wdm--interface.md">INTERFACE</a> structure.</p>
</dd>

### -field DxgkDdiOPMGetCertificateSize

<dd>
<p>A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-certificate-size.md">DxgkDdiOPMGetCertificateSize</a> function.</p>
</dd>

### -field DxgkDdiOPMGetCertificate

<dd>
<p>A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-certificate.md">DxgkDdiOPMGetCertificate</a> function.</p>
</dd>

### -field DxgkDdiOPMCreateProtectedOutput

<dd>
<p>A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-create-protected-output.md">DxgkDdiOPMCreateProtectedOutput</a> function.</p>
</dd>

### -field DxgkDdiOPMGetRandomNumber

<dd>
<p>A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-random-number.md">DxgkDdiOPMGetRandomNumber</a> function.</p>
</dd>

### -field DxgkDdiOPMSetSigningKeyAndSequenceNumbers

<dd>
<p>A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-set-signing-key-and-sequence-numbers.md">DxgkDdiOPMSetSigningKeyAndSequenceNumbers</a> function.</p>
</dd>

### -field DxgkDdiOPMGetInformation

<dd>
<p>A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-information.md">DxgkDdiOPMGetInformation</a> function.</p>
</dd>

### -field DxgkDdiOPMGetCOPPCompatibleInformation

<dd>
<p>A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-copp-compatible-information.md">DxgkDdiOPMGetCOPPCompatibleInformation</a> function.</p>
</dd>

### -field DxgkDdiOPMConfigureProtectedOutput

<dd>
<p>A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-configure-protected-output.md">DxgkDdiOPMConfigureProtectedOutput</a> function.</p>
</dd>

### -field DxgkDdiOPMDestroyProtectedOutput

<dd>
<p>A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-destroy-protected-output.md">DxgkDdiOPMDestroyProtectedOutput</a> function.</p>
</dd>
</dl>

## -remarks
<p>A kernel-mode component that must use the OPM interface initiates a call to the display miniport driver's <a href="display.dxgkddiqueryinterface">DxgkDdiQueryInterface</a> function to retrieve the interface.</p>

<p>For more information on how to use this structure with the OPM interface, see <a href="https://msdn.microsoft.com/84218245-f5f3-4a6f-88ed-9cd5db224e30">Retrieving the OPM DDI</a>.</p>

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
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-configure-protected-output.md">DxgkDdiOPMConfigureProtectedOutput</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-create-protected-output.md">DxgkDdiOPMCreateProtectedOutput</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-certificate.md">DxgkDdiOPMGetCertificate</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-destroy-protected-output.md">DxgkDdiOPMDestroyProtectedOutput</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-certificate-size.md">DxgkDdiOPMGetCertificateSize</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-copp-compatible-information.md">DxgkDdiOPMGetCOPPCompatibleInformation</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-information.md">DxgkDdiOPMGetInformation</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-random-number.md">DxgkDdiOPMGetRandomNumber</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-set-signing-key-and-sequence-numbers.md">DxgkDdiOPMSetSigningKeyAndSequenceNumbers</a>
</dt>
<dt>
<a href="display.dxgkddiqueryinterface">DxgkDdiQueryInterface</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--interface.md">INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_OPM_INTERFACE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
