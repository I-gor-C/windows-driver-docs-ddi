---
UID : NF:strmini.StreamClassGetNextEvent
title : StreamClassGetNextEvent function
author : windows-driver-content
description : Minidrivers can use the StreamClassGetNextEvent routine to search the event queue of a device or of a particular stream.
old-location : stream\streamclassgetnextevent.htm
old-project : stream
ms.assetid : a2f83163-4529-4627-8959-2b4cd6b88828
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : StreamClassGetNextEvent
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : strmini.h
req.include-header : Strmini.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : StreamClassGetNextEvent
req.alt-loc : Stream.lib,Stream.dll
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Stream.lib
req.dll : 
req.irql : 
req.typenames : STREAM_PRIORITY, *PSTREAM_PRIORITY
req.product : Windows 10 or later.
---


# StreamClassGetNextEvent function
Minidrivers can use the <b>StreamClassGetNextEvent</b> routine to search the event queue of a device or of a particular stream.

## Syntax

````
PKSEVENT_ENTRY StreamClassGetNextEvent(
  _In_opt_ PVOID             HwDeviceExtension,
  _In_opt_ PHW_STREAM_OBJECT HwStreamObject,
  _In_opt_ GUID              *EventGuid,
  _In_     ULONG             EventItem,
  _In_opt_ PKSEVENT_ENTRY    CurrentEvent
);
````

## Parameters

`HwInstanceExtension_OR_HwDeviceExtension`



`HwStreamObject`

Pointer to a <a href="..\strmini\ns-strmini-_hw_stream_object.md">HW_STREAM_OBJECT</a>. Set to <b>NULL</b> to search the event queue of the device itself. To search the event queue of a particular stream, set to the stream's stream object.

`EventGuid`

Specifies the event set to match when walking the queue, or <b>NULL</b> to match any event set.

`EventItem`

Specifies the event ID to match when walking the queue, or -1 to match any event.

`CurrentEvent`

Pointer to an event in the event queue, or <b>NULL</b>.


## Return Value

If <i>CurrentEvent</i> is not <b>NULL</b>, <b>StreamClassGetNextEvent</b> returns the next matching event after <i>CurrentEvent</i> in the queue (or <b>NULL</b> if there is no such next event). If <i>CurrentEvent</i> is <b>NULL</b>, <b>StreamClassGetNextEvent</b> returns the first matching event in the queue.

## Remarks

The minidriver can call <b>StreamClassGetNextEvent</b> successively to loop through the event queue, examining one event at a time.

The caller may specify additional search criteria to match events on the event queue.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | strmini.h (include Strmini.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |