---
UID: NF.drmk.DrmForwardContentToDeviceObject
title: DrmForwardContentToDeviceObject
author: windows-driver-content
description: The DrmForwardContentToDeviceObject function accepts a device object representing a device to which the caller intends to forward protected content.
old-location: audio\drmforwardcontenttodeviceobject.htm
old-project: audio
ms.assetid: 1ce67fb6-190e-4de2-9877-f06cd08cf424
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: DrmForwardContentToDeviceObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: drmk.h
req.include-header: Drmk.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DrmForwardContentToDeviceObject
req.alt-loc: Drmk.lib,Drmk.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Drmk.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DrmForwardContentToDeviceObject function



## -description
<p>The <code>DrmForwardContentToDeviceObject</code> function accepts a device object representing a device to which the caller intends to forward protected content. The function authenticates the device and sends it the content ID and DRM rights that the system has assigned to the protected content.</p>


## -syntax

````
NTSTATUS DrmForwardContentToDeviceObject(
  _In_     ULONG        ContentId,
  _In_opt_ PVOID        Reserved,
  _In_     PCDRMFORWARD DrmForward
);
````


## -parameters
<dl>

### -param <i>ContentId</i> [in]

<dd>
<p>Specifies the DRM content ID. This parameter identifies a protected KS audio stream.</p>
</dd>

### -param <i>Reserved</i> [in, optional]

<dd>
<p>Reserved for future use. Set to <b>NULL</b>.</p>
</dd>

### -param <i>DrmForward</i> [in]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff536350">DRMFORWARD</a> structure specifying a device object and file object that identify the target device and a KS audio pin on that device, respectively. The structure also contains the context value that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537351">KSPROPERTY_DRMAUDIOSTREAM_CONTENTID</a>set-property request passes to the device.</p>
</dd>
</dl>

## -returns
<p><code>DrmForwardContentToDeviceObject</code> returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>Before allowing protected content to flow through a data path, the system verifies that the data path is secure. To do so, the system authenticates each module in the data path beginning at the upstream end of the data path and moving downstream. As each module is authenticated, that module gives the system information about the next module in the data path so that it can also be authenticated. To be successfully authenticated, a module's binary file must be signed as DRM-compliant.</p>

<p>Two adjacent modules in the data path can communicate with each other in one of several ways. If the upstream module calls the downstream module through <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a>, the downstream module is part of a WDM driver. In this case, the upstream module calls the <code>DrmForwardContentToDeviceObject</code> function to provide the system with the device object representing the downstream module. (If the two modules communicate through the downstream module's COM interface or content handlers, the upstream module calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff536353">DrmForwardContentToInterface</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff536347">DrmAddContentHandlers</a> instead.)</p>

<p>The caller fills in the <b>DeviceObject</b>, <b>FileObject</b>, and <b>Context</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536350">DRMFORWARD</a> structure that parameter <i>DrmForward</i> points to. <code>DrmForwardContentToDeviceObject</code> uses these values as follows:</p>

<p><b>DeviceObject</b> specifies the device object that represents the driver (the downstream module). <code>DrmForwardContentToDeviceObject</code> uses the device object to authenticate the driver. If successful, the function sets the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537351">KSPROPERTY_DRMAUDIOSTREAM_CONTENTID</a> property on the device by sending a set-property request to a KS pin on the device.</p>

<p><b>FileObject</b> specifies the KS pin to which <code>DrmForwardContentToDeviceObject</code> sends the property request.</p>

<p><b>Context</b> specifies a context value that the caller passes to the driver through the property request. <code>DrmForwardContentToDeviceObject</code> copies the context value into the request's property descriptor. The context value is typically a pointer to a buffer containing data in some custom format that both the caller and driver understand. By convention, if the downstream module is a KS filter, the <b>Context</b> member points to a file object that specifies the KS pin to which the <code>DrmForwardContentToDeviceObject</code> function sends the property request. In other words, the <b>Context</b> member points to the same file object as the <b>FileObject</b> member. USB audio drivers must set the <b>Context</b> parameter to a USBD_PIPE_HANDLE value.</p>

<p>The property request also contains the DRM content ID from parameter <i>ContentId</i> and the DRM content rights belonging to that content ID. <code>DrmForwardContentToDeviceObject</code> copies these values into the request's property value. <code>DrmForwardContentToDeviceObject</code> makes no further use of the device object after returning.</p>

<p><code>DrmForwardContentToDeviceObject</code> performs the same function as <a href="https://msdn.microsoft.com/library/windows/hardware/ff537696">PcForwardContentToDeviceObject</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff536579">IDrmPort2::ForwardContentToDeviceObject</a>. For more information, see <a href="NULL">DRM Functions and Interfaces</a>.</p>

<p>The KSPROPERTY_DRMAUDIOSTREAM_CONTENTID property assigns the DRM content ID and DRM content rights to a KS audio pin.</p>

<p>No</p>

<p>Yes</p>

<p>Pin</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537492">KSP_DRMAUDIOSTREAM_CONTENTID</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537099">KSDRMAUDIOSTREAM_CONTENTID</a>
</p>

<p> </p>

<p>The property value (operation data) is a KSDRMAUDIOSTREAM_CONTENTID structure that specifies the stream's DRM content ID and DRM content rights.</p>

<p>A KSPROPERTY_DRMAUDIOSTREAM_CONTENTID property request returns a status code that indicates whether the KS filter can enforce the specified DRM content rights, as shown in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The KS audio filter enforces the specified DRM content rights.</p>

<p>STATUS_NOT_IMPLEMENTED</p>

<p>The KS filter cannot enforce the specified DRM content rights.</p>

<p> </p>

<p>The <b>DrmForwardContentToDeviceObject</b> function uses this property to set the DRM content ID and content rights on the audio stream entering the KS pin that is the target of the property request.</p>

<p>A KS audio filter handles this property request synchronously. If the request returns STATUS_SUCCESS, all the downstream KS audio nodes (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536219">Audio Topology Nodes</a>) of the target KS audio pin were also successfully configured with the specified DRM content ID and DRM content rights. (Note that a downstream node is a direct or indirect sink for the audio content flowing through an audio pin.)</p>

<p>The DRM system can set this property at any time during the lifetime of the file object that represents a KS audio pin. If the request does not succeed, the previously set DRM content ID and DRM content rights remain in effect on the KS audio stream.</p>

<p>The handler for the KSPROPERTY_DRMAUDIOSTREAM_CONTENTID property must verify that the property-request IRP originates in kernel mode (that is, confirm that the IRP's <b>RequestorMode</b> field equals <b>KernelMode</b>). If the IRP originates in user mode, the handler must fail the IRP and return status code INVALID_DEVICE_REQUEST.</p>

<p><b>DrmForwardContentToDeviceObject</b> is an entry point in the <a href="audio.kernel_mode_wdm_audio_components#drmk_system_driver#drmk_system_driver">DRMK system driver</a>, Drmk.sys. DRMK sends an IOCTL_KS_PROPERTY request for the KSPROPERTY_DRMAUDIOSTREAM_CONTENTID property at IRQL PASSIVE_LEVEL.</p>

<p>Before allowing protected content to flow through a data path, the system verifies that the data path is secure. To do so, the system authenticates each module in the data path beginning at the upstream end of the data path and moving downstream. As each module is authenticated, that module gives the system information about the next module in the data path so that it can also be authenticated. To be successfully authenticated, a module's binary file must be signed as DRM-compliant.</p>

<p>Two adjacent modules in the data path can communicate with each other in one of several ways. If the upstream module calls the downstream module through <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a>, the downstream module is part of a WDM driver. In this case, the upstream module calls the <code>DrmForwardContentToDeviceObject</code> function to provide the system with the device object representing the downstream module. (If the two modules communicate through the downstream module's COM interface or content handlers, the upstream module calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff536353">DrmForwardContentToInterface</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff536347">DrmAddContentHandlers</a> instead.)</p>

<p>The caller fills in the <b>DeviceObject</b>, <b>FileObject</b>, and <b>Context</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536350">DRMFORWARD</a> structure that parameter <i>DrmForward</i> points to. <code>DrmForwardContentToDeviceObject</code> uses these values as follows:</p>

<p><b>DeviceObject</b> specifies the device object that represents the driver (the downstream module). <code>DrmForwardContentToDeviceObject</code> uses the device object to authenticate the driver. If successful, the function sets the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537351">KSPROPERTY_DRMAUDIOSTREAM_CONTENTID</a> property on the device by sending a set-property request to a KS pin on the device.</p>

<p><b>FileObject</b> specifies the KS pin to which <code>DrmForwardContentToDeviceObject</code> sends the property request.</p>

<p><b>Context</b> specifies a context value that the caller passes to the driver through the property request. <code>DrmForwardContentToDeviceObject</code> copies the context value into the request's property descriptor. The context value is typically a pointer to a buffer containing data in some custom format that both the caller and driver understand. By convention, if the downstream module is a KS filter, the <b>Context</b> member points to a file object that specifies the KS pin to which the <code>DrmForwardContentToDeviceObject</code> function sends the property request. In other words, the <b>Context</b> member points to the same file object as the <b>FileObject</b> member. USB audio drivers must set the <b>Context</b> parameter to a USBD_PIPE_HANDLE value.</p>

<p>The property request also contains the DRM content ID from parameter <i>ContentId</i> and the DRM content rights belonging to that content ID. <code>DrmForwardContentToDeviceObject</code> copies these values into the request's property value. <code>DrmForwardContentToDeviceObject</code> makes no further use of the device object after returning.</p>

<p><code>DrmForwardContentToDeviceObject</code> performs the same function as <a href="https://msdn.microsoft.com/library/windows/hardware/ff537696">PcForwardContentToDeviceObject</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff536579">IDrmPort2::ForwardContentToDeviceObject</a>. For more information, see <a href="NULL">DRM Functions and Interfaces</a>.</p>

<p>The KSPROPERTY_DRMAUDIOSTREAM_CONTENTID property assigns the DRM content ID and DRM content rights to a KS audio pin.</p>

<p>No</p>

<p>Yes</p>

<p>Pin</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537492">KSP_DRMAUDIOSTREAM_CONTENTID</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537099">KSDRMAUDIOSTREAM_CONTENTID</a>
</p>

<p> </p>

<p>The property value (operation data) is a KSDRMAUDIOSTREAM_CONTENTID structure that specifies the stream's DRM content ID and DRM content rights.</p>

<p>A KSPROPERTY_DRMAUDIOSTREAM_CONTENTID property request returns a status code that indicates whether the KS filter can enforce the specified DRM content rights, as shown in the following table.</p>

<p>STATUS_SUCCESS</p>

<p>The KS audio filter enforces the specified DRM content rights.</p>

<p>STATUS_NOT_IMPLEMENTED</p>

<p>The KS filter cannot enforce the specified DRM content rights.</p>

<p> </p>

<p>The <b>DrmForwardContentToDeviceObject</b> function uses this property to set the DRM content ID and content rights on the audio stream entering the KS pin that is the target of the property request.</p>

<p>A KS audio filter handles this property request synchronously. If the request returns STATUS_SUCCESS, all the downstream KS audio nodes (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536219">Audio Topology Nodes</a>) of the target KS audio pin were also successfully configured with the specified DRM content ID and DRM content rights. (Note that a downstream node is a direct or indirect sink for the audio content flowing through an audio pin.)</p>

<p>The DRM system can set this property at any time during the lifetime of the file object that represents a KS audio pin. If the request does not succeed, the previously set DRM content ID and DRM content rights remain in effect on the KS audio stream.</p>

<p>The handler for the KSPROPERTY_DRMAUDIOSTREAM_CONTENTID property must verify that the property-request IRP originates in kernel mode (that is, confirm that the IRP's <b>RequestorMode</b> field equals <b>KernelMode</b>). If the IRP originates in user mode, the handler must fail the IRP and return status code INVALID_DEVICE_REQUEST.</p>

<p><b>DrmForwardContentToDeviceObject</b> is an entry point in the <a href="audio.kernel_mode_wdm_audio_components#drmk_system_driver#drmk_system_driver">DRMK system driver</a>, Drmk.sys. DRMK sends an IOCTL_KS_PROPERTY request for the KSPROPERTY_DRMAUDIOSTREAM_CONTENTID property at IRQL PASSIVE_LEVEL.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Drmk.h (include Drmk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Drmk.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536350">DRMFORWARD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536353">DrmForwardContentToInterface</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536347">DrmAddContentHandlers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537351">KSPROPERTY_DRMAUDIOSTREAM_CONTENTID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537696">PcForwardContentToDeviceObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536579">IDrmPort2::ForwardContentToDeviceObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20DrmForwardContentToDeviceObject function%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
