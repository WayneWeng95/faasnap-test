# Go API client for swagger

FaaSnap API

## Overview
This API client was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project.  By using the [swagger-spec](https://github.com/swagger-api/swagger-spec) from a remote server, you can easily generate an API client.

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.GoClientCodegen

## Installation
Put the package under your project folder and add the following in import:
```golang
import "./swagger"
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8080*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**FunctionsGet**](docs/DefaultApi.md#functionsget) | **Get** /functions | 
*DefaultApi* | [**FunctionsPost**](docs/DefaultApi.md#functionspost) | **Post** /functions | 
*DefaultApi* | [**InvocationsPost**](docs/DefaultApi.md#invocationspost) | **Post** /invocations | 
*DefaultApi* | [**MetricsGet**](docs/DefaultApi.md#metricsget) | **Get** /metrics | 
*DefaultApi* | [**NetIfacesNamespacePut**](docs/DefaultApi.md#netifacesnamespaceput) | **Put** /net-ifaces/{namespace} | 
*DefaultApi* | [**SnapshotsPost**](docs/DefaultApi.md#snapshotspost) | **Post** /snapshots | 
*DefaultApi* | [**SnapshotsPut**](docs/DefaultApi.md#snapshotsput) | **Put** /snapshots | 
*DefaultApi* | [**SnapshotsSsIdMincoreGet**](docs/DefaultApi.md#snapshotsssidmincoreget) | **Get** /snapshots/{ssId}/mincore | 
*DefaultApi* | [**SnapshotsSsIdMincorePatch**](docs/DefaultApi.md#snapshotsssidmincorepatch) | **Patch** /snapshots/{ssId}/mincore | 
*DefaultApi* | [**SnapshotsSsIdMincorePost**](docs/DefaultApi.md#snapshotsssidmincorepost) | **Post** /snapshots/{ssId}/mincore | 
*DefaultApi* | [**SnapshotsSsIdMincorePut**](docs/DefaultApi.md#snapshotsssidmincoreput) | **Put** /snapshots/{ssId}/mincore | 
*DefaultApi* | [**SnapshotsSsIdPatch**](docs/DefaultApi.md#snapshotsssidpatch) | **Patch** /snapshots/{ssId} | 
*DefaultApi* | [**SnapshotsSsIdReapDelete**](docs/DefaultApi.md#snapshotsssidreapdelete) | **Delete** /snapshots/{ssId}/reap | 
*DefaultApi* | [**SnapshotsSsIdReapGet**](docs/DefaultApi.md#snapshotsssidreapget) | **Get** /snapshots/{ssId}/reap | 
*DefaultApi* | [**SnapshotsSsIdReapPatch**](docs/DefaultApi.md#snapshotsssidreappatch) | **Patch** /snapshots/{ssId}/reap | 
*DefaultApi* | [**UiDataGet**](docs/DefaultApi.md#uidataget) | **Get** /ui/data | 
*DefaultApi* | [**UiGet**](docs/DefaultApi.md#uiget) | **Get** /ui | 
*DefaultApi* | [**VmmsPost**](docs/DefaultApi.md#vmmspost) | **Post** /vmms | 
*DefaultApi* | [**VmsGet**](docs/DefaultApi.md#vmsget) | **Get** /vms | 
*DefaultApi* | [**VmsPost**](docs/DefaultApi.md#vmspost) | **Post** /vms | 
*DefaultApi* | [**VmsVmIdDelete**](docs/DefaultApi.md#vmsvmiddelete) | **Delete** /vms/{vmId} | 
*DefaultApi* | [**VmsVmIdGet**](docs/DefaultApi.md#vmsvmidget) | **Get** /vms/{vmId} | 


## Documentation For Models

 - [Function](docs/Function.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [Invocation](docs/Invocation.md)
 - [Layer](docs/Layer.md)
 - [ModelInterface](docs/ModelInterface.md)
 - [Snapshot](docs/Snapshot.md)
 - [State](docs/State.md)
 - [State1](docs/State1.md)
 - [Vm](docs/Vm.md)
 - [Vm1](docs/Vm1.md)
 - [Vmm](docs/Vmm.md)


## Documentation For Authorization
 Endpoints do not require authorization.


## Author



