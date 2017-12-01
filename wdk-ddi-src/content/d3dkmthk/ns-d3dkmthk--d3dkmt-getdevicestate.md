---
UID: NS.d3dkmthk._D3DKMT_GETDEVICESTATE
title: D3DKMT_GETDEVICESTATE
author: windows-driver-content
description: The D3DKMT_GETDEVICESTATE structure describes parameters for retrieving the state of a device.
old-location: display\d3dkmt_getdevicestate.htm
old-project: display
ms.assetid: b90f8b63-51d3-4de4-9d8b-91926150fd30
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_GETDEVICESTATE, D3DKMT_GETDEVICESTATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_GETDEVICESTATE
req.alt-loc: d3dkmthk.h
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

# D3DKMT_GETDEVICESTATE structure



## -description
<p>The D3DKMT_GETDEVICESTATE structure describes parameters for retrieving the state of a device. </p>


## -syntax

````
typedef struct _D3DKMT_GETDEVICESTATE {
  D3DKMT_HANDLE           hDevice;
  D3DKMT_DEVICESTATE_TYPE StateType;
  union {
    D3DKMT_DEVICEEXECUTION_STATE ExecutionState;
    D3DKMT_DEVICEPRESENT_STATE   PresentState;
    D3DKMT_DEVICERESET_STATE     ResetState;
  };
} D3DKMT_GETDEVICESTATE;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A handle to the device that status is requested for.</p>
</dd>

### -field <b>StateType</b>

<dd>
<p>[in] A <a href="..\d3dkmthk\ne-d3dkmthk--d3dkmt-devicestate-type.md">D3DKMT_DEVICESTATE_TYPE</a>-typed value that indicates the type of status to retrieve for the device.</p>
</dd>

### -field <b>ExecutionState</b>

<dd>
<p>[out] A <a href="..\d3dkmthk\ne-d3dkmthk--d3dkmt-deviceexecution-state.md">D3DKMT_DEVICEEXECUTION_STATE</a>-typed value that indicates the execution status of the device. The union that is contained in D3DKMT_GETDEVICESTATE holds a value from this enumeration if the <b>StateType</b> member is D3DKMT_DEVICESTATE_EXECUTION. </p>
</dd>

### -field <b>PresentState</b>

<dd>
<p>[in/out] A <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-devicepresent-state.md">D3DKMT_DEVICEPRESENT_STATE</a> structure that describes parameters for retrieving the present status of the device. The union that is contained in D3DKMT_GETDEVICESTATE holds a structure of this type if the <b>StateType</b> member is D3DKMT_DEVICESTATE_PRESENT. </p>
</dd>

### -field <b>ResetState</b>

<dd>
<p>[out] A <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-devicereset-state.md">D3DKMT_DEVICERESET_STATE</a> structure that describes the reset status of the device. The union that is contained in D3DKMT_GETDEVICESTATE holds a structure of this type if the <b>StateType</b> member is D3DKMT_DEVICESTATE_RESET. </p>
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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmthk\ne-d3dkmthk--d3dkmt-deviceexecution-state.md">D3DKMT_DEVICEEXECUTION_STATE</a>
</dt>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-devicepresent-state.md">D3DKMT_DEVICEPRESENT_STATE</a>
</dt>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-devicereset-state.md">D3DKMT_DEVICERESET_STATE</a>
</dt>
<dt>
<a href="..\d3dkmthk\ne-d3dkmthk--d3dkmt-devicestate-type.md">D3DKMT_DEVICESTATE_TYPE</a>
</dt>
<dt>
<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtgetdevicestate.md">D3DKMTGetDeviceState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_GETDEVICESTATE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
