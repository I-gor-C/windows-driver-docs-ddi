# Avcstrm.h header


This header is used by unknown technology.

Avcstrm.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [AVCSTRM_BUFFER_STRUCT structure](ns-avcstrm--avcstrm-buffer-struct.md) | The AVCSTRM_BUFFER_STRUCT structure describes a buffer to be submitted to avcstrm.sys for read or write operations. |
| [AVCSTRM_FORMAT_INFO structure](ns-avcstrm--avcstrm-format-info.md) | The AVCSTRM_FORMAT_INFO structure is used to describe a data stream. |
| [AVCSTRM_OPEN_STRUCT structure](ns-avcstrm--avcstrm-open-struct.md) | The AVCSTRM_OPEN_STRUCT structure describes a data stream to be opened. |
| [AVC_STREAM_REQUEST_BLOCK structure](ns-avcstrm--avc-stream-request-block.md) | The AVC_STREAM_REQUEST_BLOCK structure describes an AV/C streaming request to be processed by avcstrm.sys. |
| [CIP_HDR1 structure](ns-avcstrm--cip-hdr1.md) | The CIP_HDR1 structure describes the generic data structure of the two quadlet CIP headers (first quadlet of the pair). |
| [CIP_HDR2_FDF structure](ns-avcstrm--cip-hdr2-fdf.md) | The CIP_HDR2_FDF structure describes the second quadlet of a CIP header pair. |
| [CIP_HDR2_MPEGTS structure](ns-avcstrm--cip-hdr2-mpegts.md) | The CIP_HDR2_MPEGTS structure describes the second quadlet of a CIP header pair for an MPEGTS format stream. |
| [CIP_HDR2_SYT structure](ns-avcstrm--cip-hdr2-syt.md) | The CIP_HDR2_SYT structure describes the second quadlet of a CIP header pair for a DV format stream. |
| [DVINFO structure](ns-avcstrm--dvinfo.md) | The DVINFO structure describes a DV stream format including its default streaming source information and stream control information. |
| [tagKS_DATAFORMAT_DV_AVC structure](ns-avcstrm-tagks-dataformat-dv-avc.md) | The KS_DATAFORMAT_DV_AVC structure stores the data format for an AV/C digital video connection. |
| [tagKS_DATAFORMAT_MPEG2TS_AVC structure](ns-avcstrm-tagks-dataformat-mpeg2ts-avc.md) | The KS_DATAFORMAT_MPEG2TS_AVC structure stores the data format for an AV/C MPEG2 connection. |
| [tagKS_DATARANGE_DVVIDEO structure](ns-avcstrm-tagks-datarange-dvvideo.md) | The KS_DATARANGE_DV_AVC structure stores a range of digital video formats. |
| [tagKS_DATARANGE_DV_AVC structure](ns-avcstrm-tagks-datarange-dv-avc.md) | The KS_DATARANGE_DV_AVC structure stores a range of AV/C digital video formats. |
| [tagKS_DATARANGE_MPEG2TS_AVC structure](ns-avcstrm-tagks-datarange-mpeg2ts-avc.md) | The KS_DATARANGE_MPEG2TS_AVC structure stores a range of AV/C MPEG2 formats. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [AVCSTRM_FORMAT enumeration](ne-avcstrm--avcstrm-format.md) | The AVCSTRM_FUNCTION enumeration defines the AV/C subunit stream formats supported by avcstrm.sys. |
| [AVCSTRM_FUNCTION enumeration](ne-avcstrm--avcstrm-function.md) | The AVCSTRM_FUNCTION enumeration defines the functionality exposed by the avcstrm.sys driver. |
