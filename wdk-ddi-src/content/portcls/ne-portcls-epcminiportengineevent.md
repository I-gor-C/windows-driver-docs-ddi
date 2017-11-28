---
UID: NE.portcls.EPcMiniportEngineEvent
title: EPcMiniportEngineEvent
author: windows-driver-content
description: This topic introduces the EPcMiniportEngineEvent enum, and describes the parameters that provide additional information when the miniport driver reports a glitching error.
old-location: audio\epcminiportengineevent.htm
old-project: audio
ms.assetid: 6B282CA4-2EE8-48BB-99E2-1A16A92E57A5
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: BarcodeSymbologyAttributesData, BarcodeSymbologyAttributesData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: portcls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EPcMiniportEngineEvent
req.alt-loc: Portcls.h
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

# EPcMiniportEngineEvent enumeration



## -description
<p>This topic introduces the EPcMiniportEngineEvent enum, and describes the parameters that provide additional information when the miniport driver reports a  glitching error.</p>
<p>The event IDs in the following enum represent events that the miniport driver can report, by using callbacks via the port class driver (PortCls).</p>


## -syntax

````
typedef enum _EPcMiniportEngineEvent { 
  eMINIPORT_IHV_DEFINED                  = 0,
  eMINIPORT_BUFFER_COMPLETE,
  eMINIPORT_PIN_STATE,
  eMINIPORT_GET_STREAM_POS,
  eMINIPORT_SET_WAVERT_BUFFER_WRITE_POS,
  eMINIPORT_GET_PRESENTATION_POS,
  eMINIPORT_PROGRAM_DMA,
  eMINIPORT_GLITCH_REPORT,
  eMINIPORT_LAST_BUFFER_RENDERED,
  eMINIPORT_PROCESSING_MODE,
  eMINIPORT_FX_CLSID,
  eMINIPORT_MaxValue
} EPcMiniportEngineEvent;
````


## -enum-fields
<dl>

### -field <a id="eMINIPORT_IHV_DEFINED"></a><a id="eminiport_ihv_defined"></a><a id="EMINIPORT_IHV_DEFINED"></a><b>eMINIPORT_IHV_DEFINED</b>

<dd>
<p>Specifies the ID for an IHV-defined event.</p>
</dd>

### -field <a id="eMINIPORT_BUFFER_COMPLETE"></a><a id="eminiport_buffer_complete"></a><a id="EMINIPORT_BUFFER_COMPLETE"></a><b>eMINIPORT_BUFFER_COMPLETE</b>

<dd>
<p>Specifies the ID for the buffer complete event.</p>
</dd>

### -field <a id="eMINIPORT_PIN_STATE"></a><a id="eminiport_pin_state"></a><a id="EMINIPORT_PIN_STATE"></a><b>eMINIPORT_PIN_STATE</b>

<dd>
<p>Specifies the ID for the event related to a change in pin state.</p>
</dd>

### -field <a id="eMINIPORT_GET_STREAM_POS"></a><a id="eminiport_get_stream_pos"></a><a id="EMINIPORT_GET_STREAM_POS"></a><b>eMINIPORT_GET_STREAM_POS</b>

<dd>
<p>Specifies the ID for a "get stream position" event.</p>
</dd>

### -field <a id="eMINIPORT_SET_WAVERT_BUFFER_WRITE_POS"></a><a id="eminiport_set_wavert_buffer_write_pos"></a><a id="EMINIPORT_SET_WAVERT_BUFFER_WRITE_POS"></a><b>eMINIPORT_SET_WAVERT_BUFFER_WRITE_POS</b>

<dd>
<p>Specifies the ID for a "wave  buffer write position" event.</p>
</dd>

### -field <a id="eMINIPORT_GET_PRESENTATION_POS"></a><a id="eminiport_get_presentation_pos"></a><a id="EMINIPORT_GET_PRESENTATION_POS"></a><b>eMINIPORT_GET_PRESENTATION_POS</b>

<dd>
<p>Specifies the ID for a "get presentation position" event.</p>
</dd>

### -field <a id="eMINIPORT_PROGRAM_DMA"></a><a id="eminiport_program_dma"></a><a id="EMINIPORT_PROGRAM_DMA"></a><b>eMINIPORT_PROGRAM_DMA</b>

<dd>
<p>Specifies the ID for a "program DMA" event.</p>
</dd>

### -field <a id="eMINIPORT_GLITCH_REPORT"></a><a id="eminiport_glitch_report"></a><a id="EMINIPORT_GLITCH_REPORT"></a><b>eMINIPORT_GLITCH_REPORT</b>

<dd>
<p>Specifies the ID for a "glitch report" event.</p>
</dd>

### -field <a id="eMINIPORT_LAST_BUFFER_RENDERED"></a><a id="eminiport_last_buffer_rendered"></a><a id="EMINIPORT_LAST_BUFFER_RENDERED"></a><b>eMINIPORT_LAST_BUFFER_RENDERED</b>

<dd>
<p>Specifies the ID for the last buffer that was rendered.</p>
</dd>

### -field <a id="eMINIPORT_PROCESSING_MODE"></a><a id="eminiport_processing_mode"></a><a id="EMINIPORT_PROCESSING_MODE"></a><b>eMINIPORT_PROCESSING_MODE</b>

<dd>
<p>Specifies the ID for the processing mode that was in effect when the glitch happened.</p>
</dd>

### -field <a id="eMINIPORT_FX_CLSID"></a><a id="eminiport_fx_clsid"></a><a id="EMINIPORT_FX_CLSID"></a><b>eMINIPORT_FX_CLSID</b>

<dd>
<p>Specifies the class ID for the audio processing effect (FX) that was in effect when the glitch happened.</p>
</dd>

### -field <a id="eMINIPORT_MaxValue"></a><a id="eminiport_maxvalue"></a><a id="EMINIPORT_MAXVALUE"></a><b>eMINIPORT_MaxValue</b>

<dd>
<p>Specifies the ID for the highest enumerated value that was used to report the glitch.</p>
</dd>
</dl>

## -remarks
<p>The following table shows the members of the  EPcMiniportEngineEvent enum that were introduced with Windows 8. The table shows the events associated with the enum's members, and the meanings of their parameters.</p>

<p>
<table>
<tr>
<th>Event type</th>
<th>Parameter 1</th>
<th>Parameter  2</th>
<th>Parameter  3</th>
<th>Parameter  4</th>
</tr>
<tr>
<td>IHV-specific event type.</td>
<td>Defined and used by IHVs.</td>
<td>Defined and used by IHVs.</td>
<td>Defined and used by IHVs.</td>
<td>Defined and used by IHVs.</td>
</tr>
<tr>
<td>Buffer complete. </td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>Data length completed.</td>
<td>0</td>
</tr>
<tr>
<td>Pin state.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>
<dl>
<dd>0 - KS_STOP</dd>
<dd>1 - KS_ACQUIRE</dd>
<dd>2 - KS_PAUSE</dd>
<dd>3 - KS_RUN</dd>
</dl>
</td>
<td>0</td>
</tr>
<tr>
<td>Get stream position.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Set WaveRT buffer write position.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position that was received from PortCls.</td>
<td>Target WaveRTBuffer write position that was received from PortCls.</td>
<td>0</td>
</tr>
<tr>
<td>Get presentation position.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>Presentation position.</td>
<td>0</td>
</tr>
<tr>
<td>Program DMA.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>Starting WaveRtBuffer offset</td>
<td>Data length.</td>
</tr>
<tr>
<td>Glitch detection.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>
<dl>
<dd>1 - WaveRT buffer under run</dd>
<dd>2 - Decoder errors</dd>
<dd>3 - Receive the same WaveRT buffer write position twice in a row.</dd>
</dl>
</td>
<td>When Parameter 3 = '3' then Parameter 4 is the offending write position.</td>
</tr>
</table>
<p> </p>
</p><dl>
<dd>0 - KS_STOP</dd>
<dd>1 - KS_ACQUIRE</dd>
<dd>2 - KS_PAUSE</dd>
<dd>3 - KS_RUN</dd>
</dl><dl>
<dd>1 - WaveRT buffer under run</dd>
<dd>2 - Decoder errors</dd>
<dd>3 - Receive the same WaveRT buffer write position twice in a row.</dd>
</dl><p> </p>

<p>The following table shows the members of the  EPcMiniportEngineEvent enum that were introduced with Windows 8.1. The table shows the events associated with the enum's members, and the meanings of their parameters.</p>

<p>
<table>
<tr>
<th>Event type</th>
<th>Parameter 1</th>
<th>Parameter  2</th>
<th>Parameter  3</th>
<th>Parameter  4</th>
</tr>
<tr>
<td>Last buffer rendered.</td>
<td>Current linear buffer position.</td>
<td>The very last WaveRtBuffer write position that the driver received.</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Processing mode.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>First 8 bytes of GUID.</td>
<td>Second 8 bytes of GUID.</td>
</tr>
<tr>
<td>FX class ID.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>First 8 bytes of FX CLSID.            </td>
<td>Second 8 bytes of FX CLSID.            </td>
</tr>
<tr>
<td>Max value.</td>
<td>ID for enumerated value.</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</table>
<p> </p>
</p>

<p> </p>

<p>The following table shows the members of the  EPcMiniportEngineEvent enum that were introduced with Windows 8. The table shows the events associated with the enum's members, and the meanings of their parameters.</p>

<p>
<table>
<tr>
<th>Event type</th>
<th>Parameter 1</th>
<th>Parameter  2</th>
<th>Parameter  3</th>
<th>Parameter  4</th>
</tr>
<tr>
<td>IHV-specific event type.</td>
<td>Defined and used by IHVs.</td>
<td>Defined and used by IHVs.</td>
<td>Defined and used by IHVs.</td>
<td>Defined and used by IHVs.</td>
</tr>
<tr>
<td>Buffer complete. </td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>Data length completed.</td>
<td>0</td>
</tr>
<tr>
<td>Pin state.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>
<dl>
<dd>0 - KS_STOP</dd>
<dd>1 - KS_ACQUIRE</dd>
<dd>2 - KS_PAUSE</dd>
<dd>3 - KS_RUN</dd>
</dl>
</td>
<td>0</td>
</tr>
<tr>
<td>Get stream position.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Set WaveRT buffer write position.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position that was received from PortCls.</td>
<td>Target WaveRTBuffer write position that was received from PortCls.</td>
<td>0</td>
</tr>
<tr>
<td>Get presentation position.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>Presentation position.</td>
<td>0</td>
</tr>
<tr>
<td>Program DMA.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>Starting WaveRtBuffer offset</td>
<td>Data length.</td>
</tr>
<tr>
<td>Glitch detection.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>
<dl>
<dd>1 - WaveRT buffer under run</dd>
<dd>2 - Decoder errors</dd>
<dd>3 - Receive the same WaveRT buffer write position twice in a row.</dd>
</dl>
</td>
<td>When Parameter 3 = '3' then Parameter 4 is the offending write position.</td>
</tr>
</table>
<p> </p>
</p><dl>
<dd>0 - KS_STOP</dd>
<dd>1 - KS_ACQUIRE</dd>
<dd>2 - KS_PAUSE</dd>
<dd>3 - KS_RUN</dd>
</dl><dl>
<dd>1 - WaveRT buffer under run</dd>
<dd>2 - Decoder errors</dd>
<dd>3 - Receive the same WaveRT buffer write position twice in a row.</dd>
</dl><p> </p>

<p>The following table shows the members of the  EPcMiniportEngineEvent enum that were introduced with Windows 8.1. The table shows the events associated with the enum's members, and the meanings of their parameters.</p>

<p>
<table>
<tr>
<th>Event type</th>
<th>Parameter 1</th>
<th>Parameter  2</th>
<th>Parameter  3</th>
<th>Parameter  4</th>
</tr>
<tr>
<td>Last buffer rendered.</td>
<td>Current linear buffer position.</td>
<td>The very last WaveRtBuffer write position that the driver received.</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Processing mode.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>First 8 bytes of GUID.</td>
<td>Second 8 bytes of GUID.</td>
</tr>
<tr>
<td>FX class ID.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>First 8 bytes of FX CLSID.            </td>
<td>Second 8 bytes of FX CLSID.            </td>
</tr>
<tr>
<td>Max value.</td>
<td>ID for enumerated value.</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</table>
<p> </p>
</p>

<p> </p>

<p>The following table shows the members of the  EPcMiniportEngineEvent enum that were introduced with Windows 8. The table shows the events associated with the enum's members, and the meanings of their parameters.</p>

<p>
<table>
<tr>
<th>Event type</th>
<th>Parameter 1</th>
<th>Parameter  2</th>
<th>Parameter  3</th>
<th>Parameter  4</th>
</tr>
<tr>
<td>IHV-specific event type.</td>
<td>Defined and used by IHVs.</td>
<td>Defined and used by IHVs.</td>
<td>Defined and used by IHVs.</td>
<td>Defined and used by IHVs.</td>
</tr>
<tr>
<td>Buffer complete. </td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>Data length completed.</td>
<td>0</td>
</tr>
<tr>
<td>Pin state.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>
<dl>
<dd>0 - KS_STOP</dd>
<dd>1 - KS_ACQUIRE</dd>
<dd>2 - KS_PAUSE</dd>
<dd>3 - KS_RUN</dd>
</dl>
</td>
<td>0</td>
</tr>
<tr>
<td>Get stream position.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Set WaveRT buffer write position.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position that was received from PortCls.</td>
<td>Target WaveRTBuffer write position that was received from PortCls.</td>
<td>0</td>
</tr>
<tr>
<td>Get presentation position.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>Presentation position.</td>
<td>0</td>
</tr>
<tr>
<td>Program DMA.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>Starting WaveRtBuffer offset</td>
<td>Data length.</td>
</tr>
<tr>
<td>Glitch detection.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>
<dl>
<dd>1 - WaveRT buffer under run</dd>
<dd>2 - Decoder errors</dd>
<dd>3 - Receive the same WaveRT buffer write position twice in a row.</dd>
</dl>
</td>
<td>When Parameter 3 = '3' then Parameter 4 is the offending write position.</td>
</tr>
</table>
<p> </p>
</p><dl>
<dd>0 - KS_STOP</dd>
<dd>1 - KS_ACQUIRE</dd>
<dd>2 - KS_PAUSE</dd>
<dd>3 - KS_RUN</dd>
</dl><dl>
<dd>1 - WaveRT buffer under run</dd>
<dd>2 - Decoder errors</dd>
<dd>3 - Receive the same WaveRT buffer write position twice in a row.</dd>
</dl><p> </p>

<p>The following table shows the members of the  EPcMiniportEngineEvent enum that were introduced with Windows 8.1. The table shows the events associated with the enum's members, and the meanings of their parameters.</p>

<p>
<table>
<tr>
<th>Event type</th>
<th>Parameter 1</th>
<th>Parameter  2</th>
<th>Parameter  3</th>
<th>Parameter  4</th>
</tr>
<tr>
<td>Last buffer rendered.</td>
<td>Current linear buffer position.</td>
<td>The very last WaveRtBuffer write position that the driver received.</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Processing mode.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>First 8 bytes of GUID.</td>
<td>Second 8 bytes of GUID.</td>
</tr>
<tr>
<td>FX class ID.</td>
<td>Current linear buffer position.</td>
<td>Current WaveRTBuffer write position.</td>
<td>First 8 bytes of FX CLSID.            </td>
<td>Second 8 bytes of FX CLSID.            </td>
</tr>
<tr>
<td>Max value.</td>
<td>ID for enumerated value.</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</table>
<p> </p>
</p>

<p> </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="NULL">Glitch Reporting for Offloaded Audio</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265124">MiniportWriteEtwEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20EPcMiniportEngineEvent enumeration%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
