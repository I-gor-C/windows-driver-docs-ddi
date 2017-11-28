---
UID: NS.ksmedia.tagTRANSPORTBASICPARMS
title: tagTRANSPORTBASICPARMS
author: windows-driver-content
description: The TRANSPORTBASICPARMS structure is defined but not used.
old-location: stream\transportbasicparms.htm
old-project: stream
ms.assetid: 40e305b3-e91c-4227-99e7-dbb939082f54
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: tagTRANSPORTBASICPARMS, TRANSPORTBASICPARMS, *PTRANSPORTBASICPARMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TRANSPORTBASICPARMS
req.alt-loc: ksmedia.h
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

# tagTRANSPORTBASICPARMS structure



## -description
<p>The TRANSPORTBASICPARMS structure is defined but not used.</p>


## -syntax

````
typedef struct tagTRANSPORTBASICPARMS {
  LONG  TimeFormat;
  LONG  TimeReference;
  LONG  Superimpose;
  LONG  EndStopAction;
  LONG  RecordFormat;
  LONG  StepFrames;
  LONG  SetpField;
  LONG  Preroll;
  LONG  RecPreroll;
  LONG  Postroll;
  LONG  EditDelay;
  LONG  PlayTCDelay;
  LONG  RecTCDelay;
  LONG  EditField;
  LONG  FrameServo;
  LONG  ColorFrameServo;
  LONG  ServoRef;
  LONG  WarnGenlock;
  LONG  SetTracking;
  TCHAR VolumeName[40];
  LONG  Ballistic[20];
  LONG  Speed;
  LONG  CounterFormat;
  LONG  TunerChannel;
  LONG  TunerNumber;
  LONG  TimerEvent;
  LONG  TimerStartDay;
  LONG  TimerStartTime;
  LONG  TimerStopDay;
  LONG  TimerStopTime;
} TRANSPORTBASICPARMS, *PTRANSPORTBASICPARMS;
````


## -struct-fields
<dl>

### -field <b>TimeFormat</b>

<dd>
<p>Indicates the basic time format.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>ED_FORMAT_MILLISECONDS</p>
</td>
<td>
<p>Milliseconds</p>
</td>
</tr>
<tr>
<td>
<p>ED_FORMAT_FRAMES</p>
</td>
<td>
<p>Frames</p>
</td>
</tr>
<tr>
<td>
<p>ED_FORMAT_REFERENCE_TIME</p>
</td>
<td>
<p>Reference time</p>
</td>
</tr>
<tr>
<td>
<p>ED_FORMAT_HMSF</p>
</td>
<td>
<p>Binary coded decimal, representing hours, minutes, seconds, and frames</p>
</td>
</tr>
<tr>
<td>
<p>ED_FORMAT_TMSF</p>
</td>
<td>
<p>Binary coded decimal, representing tracks, minutes, seconds, and frames</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>TimeReference</b>

<dd>
<p>Indicates the basic time reference.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>ED_TIMEREF_TIMECODE</p>
</td>
<td>
<p>Time code</p>
</td>
</tr>
<tr>
<td>
<p>ED_TIMEREF_CONTROL_TRACK</p>
</td>
<td>
<p>Control track</p>
</td>
</tr>
<tr>
<td>
<p>ED_TIMEREF_INDEX</p>
</td>
<td>
<p>Index</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Superimpose</b>

<dd>
<p>Indicates whether to enable or disable the onscreen display. Specify <b>TRUE</b> to enable, <b>FALSE</b> to disable.</p>
</dd>

### -field <b>EndStopAction</b>

<dd>
<p>Specifies the stop action.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>ED_MODE_STOP</p>
</td>
<td>
<p>Stop</p>
</td>
</tr>
<tr>
<td>
<p>ED_MODE_REWIND</p>
</td>
<td>
<p>Rewind</p>
</td>
</tr>
<tr>
<td>
<p>ED_MODE_FREEZE</p>
</td>
<td>
<p>Freeze/pause</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>RecordFormat</b>

<dd>
<p>Indicates the basic record format.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>ED_RECORD_FORMAT_SP</p>
</td>
<td>
<p>Standard play</p>
</td>
</tr>
<tr>
<td>
<p>ED_RECORD_FORMAT_LP</p>
</td>
<td>
<p>Long play</p>
</td>
</tr>
<tr>
<td>
<p>ED_RECORD_FORMAT_EP</p>
</td>
<td>
<p>Extended play</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>StepFrames</b>

<dd>
<p>Indicates the frame step count.</p>
</dd>

### -field <b>SetpField</b>

<dd>
<p>Indicates the field step count.</p>
</dd>

### -field <b>Preroll</b>

<dd>
<p>Indicates the preroll amount.</p>
</dd>

### -field <b>RecPreroll</b>

<dd>
<p>Indicates the record preroll amount.</p>
</dd>

### -field <b>Postroll</b>

<dd>
<p>Indicates the postroll amount.</p>
</dd>

### -field <b>EditDelay</b>

<dd>
<p>Indicates the edit delay amount.</p>
</dd>

### -field <b>PlayTCDelay</b>

<dd>
<p>Indicates the play timecode delay amount.</p>
</dd>

### -field <b>RecTCDelay</b>

<dd>
<p>Indicates the record timecode delay amount.</p>
</dd>

### -field <b>EditField</b>

<dd>
<p>Indicates the edit field.</p>
</dd>

### -field <b>FrameServo</b>

<dd>
<p>Specifies the frame servo.</p>
</dd>

### -field <b>ColorFrameServo</b>

<dd>
<p>Specifies the color frame servo.</p>
</dd>

### -field <b>ServoRef</b>

<dd>
<p>Specifies the servo ref.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>ED_REF_EXTERNAL</p>
</td>
<td>
<p>External</p>
</td>
</tr>
<tr>
<td>
<p>ED_REF_INPUT</p>
</td>
<td>
<p>Input</p>
</td>
</tr>
<tr>
<td>
<p>ED_REF_INTERNAL</p>
</td>
<td>
<p>Internal</p>
</td>
</tr>
<tr>
<td>
<p>ED_REF_AUTO</p>
</td>
<td>
<p>Auto</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>WarnGenlock</b>

<dd>
<p>Indicates the warn genlock.</p>
</dd>

### -field <b>SetTracking</b>

<dd>
<p>Specifies the tracking.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>ED_TRACKING_PLUS</p>
</td>
<td>
<p>Plus</p>
</td>
</tr>
<tr>
<td>
<p>ED_TRACKING_MINUS</p>
</td>
<td>
<p>Minus</p>
</td>
</tr>
<tr>
<td>
<p>ED_TRACKING_RESET</p>
</td>
<td>
<p>Reset</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>VolumeName</b>

<dd>
<p>Specifies the volume name.</p>
</dd>

### -field <b>Ballistic</b>

<dd>
<p>Specifies any proprietary data.</p>
</dd>

### -field <b>Speed</b>

<dd>
<p>Specifies the speed.</p>
</dd>

### -field <b>CounterFormat</b>

<dd>
<p>Specifies the counter format.</p>
</dd>

### -field <b>TunerChannel</b>

<dd>
<p>Indicates the tuner channel.</p>
</dd>

### -field <b>TunerNumber</b>

<dd>
<p>Indicates the tuner number.</p>
</dd>

### -field <b>TimerEvent</b>

<dd>
<p>Specifies a timer event.</p>
</dd>

### -field <b>TimerStartDay</b>

<dd>
<p>Indicates the timer start-day.</p>
</dd>

### -field <b>TimerStartTime</b>

<dd>
<p>Indicates the timer start-time.</p>
</dd>

### -field <b>TimerStopDay</b>

<dd>
<p>Indicates the timer stop-day.</p>
</dd>

### -field <b>TimerStopTime</b>

<dd>
<p>Indicates the timer stop-time.</p>
</dd>
</dl>

## -remarks
<p>Any ED_<i>Xxx</i> tokens are defined in <i>xprtdefs.h</i> in the Microsoft DirectX SDK.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>