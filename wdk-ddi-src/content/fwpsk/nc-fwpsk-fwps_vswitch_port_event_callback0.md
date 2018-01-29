---
UID : NC:fwpsk.FWPS_VSWITCH_PORT_EVENT_CALLBACK0
title : FWPS_VSWITCH_PORT_EVENT_CALLBACK0
author : windows-driver-content
description : The filter engine calls the vSwitchPortEventNotifyFn (FWPS_VSWITCH_PORT_EVENT_CALLBACK0) callout function to notify the callout driver about events that are associated a virtual switch (vSwitch) port.Note  FWPS_VSWITCH_PORT_EVENT_CALLBACK0 is a specific version of FWPS_VSWITCH_PORT_EVENT_CALLBACK. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information.
old-location : netvista\fwps_vswitch_port_event_callback0.htm
old-project : netvista
ms.assetid : CE4B14BE-5ECA-4C2F-809C-B0DC27EC2FF2
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.fwps_vswitch_port_event_callback0, vSwitchPortEventNotifyFn callback function [Network Drivers Starting with Windows Vista], vSwitchPortEventNotifyFn, FWPS_VSWITCH_PORT_EVENT_CALLBACK0, FWPS_VSWITCH_PORT_EVENT_CALLBACK0, fwpsk/vSwitchPortEventNotifyFn
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : fwpsk.h
req.include-header : Fwpsk.h
req.target-type : Windows
req.target-min-winverclnt : Available starting with Windows 8.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : "<= DISPATCH_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : PINSTANCE_PARTIAL_INFORMATION, INSTANCE_PARTIAL_INFORMATION
---


# FWPS_VSWITCH_PORT_EVENT_CALLBACK0 callback function
The filter engine calls the 
  
  <i>vSwitchPortEventNotifyFn</i>   (<i>FWPS_VSWITCH_PORT_EVENT_CALLBACK0</i>) callout function to notify the callout driver about events that are
  associated a virtual switch (vSwitch) port.<div class="alert"><b>Note</b>  <i>FWPS_VSWITCH_PORT_EVENT_CALLBACK0</i> is a specific version of <i>FWPS_VSWITCH_PORT_EVENT_CALLBACK</i>. See <a href="https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information.</div>
<div> </div>

## Syntax

```
FWPS_VSWITCH_PORT_EVENT_CALLBACK0 FwpsVswitchPortEventCallback0;

NTSTATUS FwpsVswitchPortEventCallback0(
  void *notifyContext,
  void *completionContext,
  FWPS_VSWITCH_EVENT_TYPE eventType,
  const NDIS_SWITCH_PARAMETERS *vSwitch,
  const NDIS_SWITCH_PORT_PARAMETERS *vSwitchPort
)
{...}
```

## Parameters

`*notifyContext`



`*completionContext`



`eventType`

The type of virtual switch vSwitch event  specified as one of the <a href="..\fwpsk\ne-fwpsk-fwps_vswitch_event_type_.md">FWPS_VSWITCH_EVENT_TYPE</a> enumeration values. For more information, see Remarks.

`*vSwitch`



`*vSwitchPort`




## Return Value

A callout's 
  
  <i>FWPS_VSWITCH_PORT_EVENT_CALLBACK0</i> function returns one of the following NTSTATUS codes.
<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The callout driver accepts the notification from the filter engine.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_PENDING</b></dt>
</dl>
</td>
<td width="60%">
 The operation is pending and will be completed later.  The callout  driver will  call the <a href="..\fwpsk\nf-fwpsk-fwpsvswitchnotifycomplete0.md">FwpsvSwitchNotifyComplete0</a> function to complete the pending operation.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>Other status codes</b></dt>
</dl>
</td>
<td width="60%">
An error occurred. 

</td>
</tr>
</table>

## Remarks

A callout driver registers a 
  
  <i>vSwitchPortEventNotifyFn</i> function  by calling  
    
    the <a href="..\fwpsk\nf-fwpsk-fwpsvswitcheventssubscribe0.md">FwpsvSwitchEventsSubscribe0</a>
 function.

If the <i>vSwitchPortEventNotifyFn</i> callback is registered, the callout driver receives notifications  for port creation and deletion.

If the <i>eventType</i> parameter  is set to FWPS_VSWITCH_EVENT_PORT_CREATE, a vSwitch port was created. 
In this case, the <i>vSwitch</i> parameter identifies an <a href="..\ntddndis\ns-ntddndis-_ndis_switch_parameters.md">NDIS_SWITCH_PARAMETERS</a> structure that contains information about the virtual switch (vSwitch) and the <a href="..\ntddndis\ns-ntddndis-_ndis_switch_port_parameters.md">NDIS_SWITCH_PORT_PARAMETERS</a> parameter contains information about the port. 


A callout can return STATUS_PENDING from <i>vSwitchPortEventNotifyFn</i>. In this case, the callout  driver calls the <a href="..\fwpsk\nf-fwpsk-fwpsvswitchnotifycomplete0.md">FwpsvSwitchNotifyComplete0</a> function to complete the pending operation.

After the port is deleted, the WFP filter driver calls <i>vSwitchPortEventNotifyFn</i> with FWPS_VSWITCH_EVENT_PORT_DELETE set in the <i>eventType</i> parameter.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | fwpsk.h (include Fwpsk.h) |
| **Library** |  |
| **IRQL** | <= DISPATCH_LEVEL |
| **DDI compliance rules** |  |

## See Also

<a href="..\ntddndis\ns-ntddndis-_ndis_switch_port_parameters.md">NDIS_SWITCH_PORT_PARAMETERS</a>

<a href="..\fwpsk\ne-fwpsk-fwps_vswitch_event_type_.md">FWPS_VSWITCH_EVENT_TYPE</a>

<a href="..\ntddndis\ns-ntddndis-_ndis_switch_parameters.md">NDIS_SWITCH_PARAMETERS</a>

<a href="..\fwpsk\nf-fwpsk-fwpsvswitchnotifycomplete0.md">FwpsvSwitchNotifyComplete0</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543875">Callout Driver Callout Functions</a>

<a href="..\fwpsk\nf-fwpsk-fwpsvswitcheventssubscribe0.md">FwpsvSwitchEventsSubscribe0</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_VSWITCH_PORT_EVENT_CALLBACK0 callback function%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>