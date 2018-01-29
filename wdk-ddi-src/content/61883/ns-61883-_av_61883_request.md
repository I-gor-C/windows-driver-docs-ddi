---
UID : NS:61883._AV_61883_REQUEST
title : _AV_61883_REQUEST
author : windows-driver-content
description : The AV_61883_REQUEST structure is used to pass requests to the IEC-61883 protocol driver.
old-location : ieee\av_61883_request.htm
old-project : IEEE
ms.assetid : 697fbf86-5c99-4e35-bcb4-a6f5272cc987
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : 61883/PAV_61883_REQUEST, _AV_61883_REQUEST, PAV_61883_REQUEST structure pointer [Buses], IEEE.av_61883_request, 61883_structures_d914a3cc-63dd-4eaf-9d0f-2682e1da78c9.xml, 61883/AV_61883_REQUEST, AV_61883_REQUEST structure [Buses], *PAV_61883_REQUEST, AV_61883_REQUEST, PAV_61883_REQUEST
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : 61883.h
req.include-header : 61883.h
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
req.typenames : "*PAV_61883_REQUEST, AV_61883_REQUEST"
---

# _AV_61883_REQUEST structure
The AV_61883_REQUEST structure is used to pass requests to the IEC-61883 protocol driver.

## Syntax
````
typedef struct _AV_61883_REQUEST {
  ULONG Function;
  ULONG Version;
  ULONG Flags;
  union {
    GET_UNIT_INFO       GetUnitInfo;
    SET_UNIT_INFO       SetUnitInfo;
    CMP_GET_PLUG_HANDLE GetPlugHandle;
    CMP_GET_PLUG_STATE  GetPlugState;
    CMP_CONNECT         Connect;
    CMP_DISCONNECT      Disconnect;
    CIP_ATTACH_FRAME    AttachFrame;
    CIP_CANCEL_FRAME    CancelFrame;
    CIP_TALK            Talk;
    CIP_LISTEN          Listen;
    CIP_STOP            Stop;
    FCP_REQUEST         Request;
    FCP_RESPONSE        Response;
    FCP_SEND_REQUEST    SendRequest;
    FCP_GET_RESPONSE    GetResponse;
    FCP_GET_REQUEST     GetRequest;
    FCP_SEND_RESPONSE   SendResponse;
    SET_FCP_NOTIFY      SetFcpNotify;
    CMP_CREATE_PLUG     CreatePlug;
    CMP_DELETE_PLUG     DeletePlug;
    CMP_SET_PLUG        SetPlug;
    BUS_RESET_NOTIFY    BusResetNotify;
    SET_UNIT_DIRECTORY  SetUnitDirectory;
    CMP_MONITOR_PLUGS   MonitorPlugs;
  };
} AV_61883_REQUEST, *PAV_61883_REQUEST;
````

## Members


`Flags`

Flags specific to the request. For details, see the reference page for the request. Drivers must set this member to zero for requests that do not use flags.

`Function`

Determines the type of request. Each request type is documented under the value of <b>Function</b> in <a href="https://msdn.microsoft.com/library/windows/hardware/ff537195">IEC-61883 Protocol I/O Requests</a>.

`Version`

The device driver interface (DDI) version for the request. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff537219">INIT_61883_HEADER</a> macro initializes <b>Version</b> to CURRENT_61883_DDI_VERSION.

## Remarks
The <b>Parameters-&gt;</b><b>Others.Arguments1</b> member of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff537234">IOCTL_61883_CLASS</a> IRP points to an AV_61883_REQUEST structure. The IEC-61883 protocol driver uses the request structure to determine the type of request made by the client driver, and also to return the results of the operation. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff537195">IEC-61883 Protocol I/O Requests</a> for a description of the behavior of each request.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | 61883.h (include 61883.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537234">IOCTL_61883_CLASS</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537219">INIT_61883_HEADER</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20AV_61883_REQUEST structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>