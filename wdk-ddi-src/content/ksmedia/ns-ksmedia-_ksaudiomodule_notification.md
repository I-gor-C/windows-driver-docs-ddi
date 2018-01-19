---
UID : NS:ksmedia._KSAUDIOMODULE_NOTIFICATION
title : _KSAUDIOMODULE_NOTIFICATION
author : windows-driver-content
description : The KSAUDIOMODULE_NOTIFICATION structure describes the properties associated with audio modules change notification.
old-location : audio\ksaudiomodule_notification.htm
old-project : audio
ms.assetid : 92A9462C-0E8C-4012-9374-3437BB220502
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : _KSAUDIOMODULE_NOTIFICATION, *PKSAUDIOMODULE_NOTIFICATION, KSAUDIOMODULE_NOTIFICATION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ksmedia.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10, version 1703
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KSAUDIOMODULE_NOTIFICATION
req.alt-loc : Ksmedia.h
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
req.typenames : "*PKSAUDIOMODULE_NOTIFICATION, KSAUDIOMODULE_NOTIFICATION"
---

# _KSAUDIOMODULE_NOTIFICATION structure
The <b>KSAUDIOMODULE_NOTIFICATION</b> structure describes the  properties associated with audio  modules change notification.

## Syntax
````
typedef struct _KSAUDIOMODULE_NOTIFICATION {
  union {
    struct {
      GUID  DeviceId;
      GUID  ClassId;
      ULONG InstanceId;
      ULONG Reserved;
    } ProviderId;
    LONGLONG  Alignment;
  };
} KSAUDIOMODULE_NOTIFICATION, *PKSAUDIOMODULE_NOTIFICATION;
````

## Members


    ## Remarks
        The Audio module notification KSNOTIFICATIONID_AudioModule is defined in Ksmedia.h as shown here. 



For more information about audio modules, see  <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/audio/implementing-audio-module-communication">Implementing Audio Module Discovery</a>. </p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ksmedia.h |