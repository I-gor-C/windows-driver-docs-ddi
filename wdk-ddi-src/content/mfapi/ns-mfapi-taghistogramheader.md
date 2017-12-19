---
UID: NS.MFAPI.TAGHISTOGRAMHEADER
title: tagHistogramHeader
author: windows-driver-content
description: The HistogramHeader structure describes the blob format for MF_CAPTURE_METADATA_HISTOGRAM.
old-location: stream\histogramheader.htm
old-project: stream
ms.assetid: C41EC25A-98EF-4C35-9E5A-954C80B29DA6
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: tagHistogramHeader, HistogramHeader
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: mfapi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HistogramHeader
req.alt-loc: mfapi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
---

# tagHistogramHeader structure



## -description
The <b>HistogramHeader</b>  structure describes the blob format for <b>MF_CAPTURE_METADATA_HISTOGRAM</b>.



## -syntax

````
typedef struct tagHistogramHeader {
  ULONG         Size;
  ULONG         Bins;
  ULONG         FourCC;
  ULONG         ChannelMasks;
  HistogramGrid Grid;
} HistogramHeader;
````


## -struct-fields

### -field Size

Size of this header + (<a href="stream.histogramdataheader">HistogramDataHeader</a> + histogram data following) * number of channels available.


### -field Bins

Number of bins in the histogram.


### -field FourCC

Color space that the histogram is collected from


### -field ChannelMasks

Masks of the color channels that the histogram is collected for.


### -field Grid

Grid that the histogram is collected from.


## -remarks
The <b>MF_CAPTURE_METADATA_HISTOGRAM</b> attribute contains a  histogram when a preview frame is captured.

For the <b>ChannelMasks</b> field, the following bitmasks indicate the available channels in the histogram:

Each blob can contain multiple histograms collected from different regions or different color spaces of the same frame. Each histogram in the blob is identified by its own <b>HistogramHeader</b>. Each histogram has its own region and sensor output size associated. For full frame histogram, the region will match the sensor output size specified in <a href="stream.histogramgrid">HistogramGrid</a>.

Histogram data for all available channels are grouped under one histogram. Histogram data for each channel is identified by a <a href="stream.histogramdataheader">HistogramDataHeader</a> immediate above the data. <b>ChannelMasks</b> indicate how many and what channels are having the histogram data, which is the bitwise OR of the supported <b>MF_HISTOGRAM_CHANNEL_*</b> bitmasks as defined above. <b>ChannelMask</b> indicates what channel the data is for, which is identified by any one of the <b>MF_HISTOGRAM_CHANNEL_*</b> bitmasks.

Histogram data is an array of <b>ULONG</b> with each entry representing the number of pixels falling under a set of tonal values as categorized by the bin.  The data in the array should start from bin 0 to bin N-1, where N is the number of bins in the histogram, for example, <b>HistogramBlobHeader.Bins</b>.

For Windows 10, if <a href="https://msdn.microsoft.com/library/windows/hardware/dn917945">KSPROPERTY_CAMERACONTROL_EXTENDED_HISTOGRAM</a> is supported, at minimum a full frame histogram with Y channel must be provided which should be the first histogram in the histogram blob.
Note that <a href="stream.histogramblobheader">HistogramBlobHeader</a>, <b>HistogramHeader</b>, <a href="stream.histogramdataheader">HistogramDataHeader</a> and Histogram data only describe the blob format for the <b>MF_CAPTURE_METADATA_HISTOGRAM</b> attribute.  The metadata item structure for the histogram (<a href="stream.kscamera_metadata_itemheader">KSCAMERA_METADATA_ITEMHEADER</a> + all histogram metadata payload) is up to driver and must be 8-byte aligned.


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Mfapi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.histogramblobheader">HistogramBlobHeader</a>
</dt>
<dt>
<a href="stream.histogramdataheader">HistogramDataHeader</a>
</dt>
<dt>
<a href="stream.histogramgrid">HistogramGrid</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20HistogramHeader structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

