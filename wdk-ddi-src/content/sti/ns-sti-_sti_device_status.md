---
UID : NS:sti._STI_DEVICE_STATUS
title : _STI_DEVICE_STATUS
author : windows-driver-content
description : The STI_DEVICE_STATUS structure is used as a parameter to the IStiDevice::GetStatus and IStiUSD::GetStatus methods.
old-location : image\sti_device_status.htm
old-project : image
ms.assetid : 40104e1f-b936-430b-9e8c-28738579f4c7
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : image.sti_device_status, sti/STI_DEVICE_STATUS, stifnc_9581d5c4-a5c5-4115-8e9e-33f3da4806c6.xml, PSTI_DEVICE_STATUS, *PSTI_DEVICE_STATUS, STI_DEVICE_STATUS structure [Imaging Devices], PSTI_DEVICE_STATUS structure pointer [Imaging Devices], sti/PSTI_DEVICE_STATUS, STI_DEVICE_STATUS, _STI_DEVICE_STATUS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : sti.h
req.include-header : Sti.h
req.target-type : Windows
req.target-min-winverclnt : 
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
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : STI_DEVICE_STATUS, *PSTI_DEVICE_STATUS
req.product : Windows 10 or later.
---

# _STI_DEVICE_STATUS structure
The STI_DEVICE_STATUS structure is used as a parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543752">IStiDevice::GetStatus</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff543823">IStiUSD::GetStatus</a> methods.

## Syntax
````
typedef struct _STI_DEVICE_STATUS {
  DWORD dwSize;
  DWORD StatusMask;
  DWORD dwOnlineState;
  DWORD dwHardwareStatusCode;
  DWORD dwEventHandlingState;
  DWORD dwPollingInterval;
} STI_DEVICE_STATUS, *PSTI_DEVICE_STATUS;
````

## Members


`dwEventHandlingState`

Contains bit flags indicating event status. The following flags are defined in <i>Sti.h</i>.

`dwHardwareStatusCode`

Optional device-specific, vendor-defined value.

`dwOnlineState`

Bit flags indicating the device's current status. The following flags are defined in <i>Sti.h</i>.

Currently use of STI_ONLINESTATE_OPERATIONAL is required, while use of all other flags is optional. (Currently, STI_ONLINESTATE_OPERATIONAL is the only flag that the still image server checks.)

`dwPollingInterval`

Time value, in milliseconds, indicating how often the device should be polled, if polling is required.

`dwSize`

Caller-supplied size, in bytes, of the STI_DEVICE_STATUS structure.

`StatusMask`

One or more caller-supplied bit flags, indicating the type of status information being requested. The following flags are defined:
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
STI_DEVSTATUS_EVENTS_STATE

</td>
<td>
The driver should fill in the <b>dwEventHandlingState</b> member.

</td>
</tr>
<tr>
<td>
STI_DEVSTATUS_ONLINE_STATE 

</td>
<td>
The driver should fill in the <b>dwOnlineState</b> member.

</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | sti.h (include Sti.h) |