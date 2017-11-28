---
UID: NI.nfcsedev.IOCTL_NFCSE_ENUM_ENDPOINTS
title: IOCTL_NFCSE_ENUM_ENDPOINTS
author: windows-driver-content
description: Returns information regarding the list of all the secure elements attached to the NFC controller.
old-location: nfpdrivers\ioctl_nfcse_enum_endpoints.htm
old-project: nfpdrivers
ms.assetid: BDE62A2B-423E-4656-91CC-5EBDE50C6BB0
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: NFCRM_SET_RADIO_STATE, NFCRM_SET_RADIO_STATE, *PNFCRM_SET_RADIO_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: nfcsedev.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_NFCSE_ENUM_ENDPOINTS
req.alt-loc: nfcsedev.h
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
req.iface: 
---

# IOCTL_NFCSE_ENUM_ENDPOINTS IOCTL



## -description
<p>
<p> Returns information regarding the list of all the secure elements attached to the NFC controller. Note that the caller must allocate an output buffer large enough to hold information regarding all the secure elements that were enumerated by the driver i.e. Total number of SEs Enumerated x Size of the SE endpoint info otherwise the driver should return a STATUS_BUFFER_OVERFLOW error code to the client with the NumberOfEndpoints field containing the number of secure elements enumerated. The GUID identifying the secure element which maybe used to refer to a particular secure element.</p>
</p>
<p> Returns information regarding the list of all the secure elements attached to the NFC controller. Note that the caller must allocate an output buffer large enough to hold information regarding all the secure elements that were enumerated by the driver i.e. Total number of SEs Enumerated x Size of the SE endpoint info otherwise the driver should return a STATUS_BUFFER_OVERFLOW error code to the client with the NumberOfEndpoints field containing the number of secure elements enumerated. The GUID identifying the secure element which maybe used to refer to a particular secure element.</p>


## -ioctlparameters

### -input-buffer
<p>None</p>

### -input-buffer-length
<p>None</p>

<p>None</p>

### -output-buffer
<p>An <a href="..\nfcsedev\ns-nfcsedev--secure-element-endpoint-list.md"> SECURE_ELEMENT_ENDPOINT_LIST</a> for each device enumerated.</p>

<p>An <a href="..\nfcsedev\ns-nfcsedev--secure-element-endpoint-list.md"> SECURE_ELEMENT_ENDPOINT_LIST</a> for each device enumerated.</p>

<p>An <a href="..\nfcsedev\ns-nfcsedev--secure-element-endpoint-list.md"> SECURE_ELEMENT_ENDPOINT_LIST</a> for each device enumerated.</p>

### -output-buffer-length


### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p> </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p> </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p> </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p> </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p> </p>

## -remarks
<p>The following are requirements that the driver must adhere to.

<ul>
<li>In the case of integrated secure element the GUID shall be a unique identifier derived from the serial number and/or other unique identification of the secure element.

</li>
<li>For external secure elements, the GUID maybe a fixed constant and identifies only the “socket” into which the secure element is connected.</li>
<li>For device host secure element, the driver shall enumerate it as a SE end point only if it supports Host Card Emulation. The GUID used for DH maybe a fixed constant defined by the driver.</li>
<li>The caller is required to allocate an output buffer large enough to hold the information about all the secure elements that were enumerated by the driver. The buffer must be equal to the total number of SEs enumerated by the driver multiplied by the size of the SE endpoint information. If the appropriate buffer isn’t allocated, the driver returns a STATUS_BUFFER_OVERFLOW error code to the client with the NumberOfEndpoints field that contains the number of secure elements enumerated.</li>
</ul>
</p>

<p>The following are requirements that the driver must adhere to.

<ul>
<li>In the case of integrated secure element the GUID shall be a unique identifier derived from the serial number and/or other unique identification of the secure element.

</li>
<li>For external secure elements, the GUID maybe a fixed constant and identifies only the “socket” into which the secure element is connected.</li>
<li>For device host secure element, the driver shall enumerate it as a SE end point only if it supports Host Card Emulation. The GUID used for DH maybe a fixed constant defined by the driver.</li>
<li>The caller is required to allocate an output buffer large enough to hold the information about all the secure elements that were enumerated by the driver. The buffer must be equal to the total number of SEs enumerated by the driver multiplied by the size of the SE endpoint information. If the appropriate buffer isn’t allocated, the driver returns a STATUS_BUFFER_OVERFLOW error code to the client with the NumberOfEndpoints field that contains the number of secure elements enumerated.</li>
</ul>
</p>

<p>The following are requirements that the driver must adhere to.

<ul>
<li>In the case of integrated secure element the GUID shall be a unique identifier derived from the serial number and/or other unique identification of the secure element.

</li>
<li>For external secure elements, the GUID maybe a fixed constant and identifies only the “socket” into which the secure element is connected.</li>
<li>For device host secure element, the driver shall enumerate it as a SE end point only if it supports Host Card Emulation. The GUID used for DH maybe a fixed constant defined by the driver.</li>
<li>The caller is required to allocate an output buffer large enough to hold the information about all the secure elements that were enumerated by the driver. The buffer must be equal to the total number of SEs enumerated by the driver multiplied by the size of the SE endpoint information. If the appropriate buffer isn’t allocated, the driver returns a STATUS_BUFFER_OVERFLOW error code to the client with the NumberOfEndpoints field that contains the number of secure elements enumerated.</li>
</ul>
</p>

<p>The following are requirements that the driver must adhere to.

<ul>
<li>In the case of integrated secure element the GUID shall be a unique identifier derived from the serial number and/or other unique identification of the secure element.

</li>
<li>For external secure elements, the GUID maybe a fixed constant and identifies only the “socket” into which the secure element is connected.</li>
<li>For device host secure element, the driver shall enumerate it as a SE end point only if it supports Host Card Emulation. The GUID used for DH maybe a fixed constant defined by the driver.</li>
<li>The caller is required to allocate an output buffer large enough to hold the information about all the secure elements that were enumerated by the driver. The buffer must be equal to the total number of SEs enumerated by the driver multiplied by the size of the SE endpoint information. If the appropriate buffer isn’t allocated, the driver returns a STATUS_BUFFER_OVERFLOW error code to the client with the NumberOfEndpoints field that contains the number of secure elements enumerated.</li>
</ul>
</p>

<p>The following are requirements that the driver must adhere to.

<ul>
<li>In the case of integrated secure element the GUID shall be a unique identifier derived from the serial number and/or other unique identification of the secure element.

</li>
<li>For external secure elements, the GUID maybe a fixed constant and identifies only the “socket” into which the secure element is connected.</li>
<li>For device host secure element, the driver shall enumerate it as a SE end point only if it supports Host Card Emulation. The GUID used for DH maybe a fixed constant defined by the driver.</li>
<li>The caller is required to allocate an output buffer large enough to hold the information about all the secure elements that were enumerated by the driver. The buffer must be equal to the total number of SEs enumerated by the driver multiplied by the size of the SE endpoint information. If the appropriate buffer isn’t allocated, the driver returns a STATUS_BUFFER_OVERFLOW error code to the client with the NumberOfEndpoints field that contains the number of secure elements enumerated.</li>
</ul>
</p>

<p>The following are requirements that the driver must adhere to.

<ul>
<li>In the case of integrated secure element the GUID shall be a unique identifier derived from the serial number and/or other unique identification of the secure element.

</li>
<li>For external secure elements, the GUID maybe a fixed constant and identifies only the “socket” into which the secure element is connected.</li>
<li>For device host secure element, the driver shall enumerate it as a SE end point only if it supports Host Card Emulation. The GUID used for DH maybe a fixed constant defined by the driver.</li>
<li>The caller is required to allocate an output buffer large enough to hold the information about all the secure elements that were enumerated by the driver. The buffer must be equal to the total number of SEs enumerated by the driver multiplied by the size of the SE endpoint information. If the appropriate buffer isn’t allocated, the driver returns a STATUS_BUFFER_OVERFLOW error code to the client with the NumberOfEndpoints field that contains the number of secure elements enumerated.</li>
</ul>
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Nfcsedev.h</dt>
</dl>
</td>
</tr>
</table>