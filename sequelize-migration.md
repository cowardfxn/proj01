# Sequelize Migration

[Official Doc](http://docs.sequelizejs.com/manual/migrations.html#installing-cli)

## Dependency
Uses `sequelize-cli`  

`npm install --save sequelize-cli`

## Migrate operations

### Initialize
Users need to initialize migrations before running migration for the first time.

`npx sequelize-cli init`

This operation will generate folders `config`, `models`, `migrations`, `seeders` under project directory by default, or according to the configurations in `.sequelizerc` file.

`config/config.js` contains migration configurations for *development*, *test* or *production* environments. The configurations include *storage*.

The configurations of different environments are matched automatically with environment variable `NODE_ENV`.

The migration scripts to execute are all in `migrations` directory, auto-generated migration script name pattern follows `TIMESTAMP-create-XXX.js`

### Migrate operations
Create new migration
`npx sequelize-cli migration:generate --name=what-change-to-implement`

Perform migration  
`npx sequelize-cli db:migrate`

Undo migration  
`npx sequelize-cli db:migrate:undo`  
Undo the latest migration by date  

To undo all migrations, use  
`npx sequelize-cli db:migrate:undo:all --to XXXXXXXXXXXXXX-create-posts.js`  
The `--to` option is to specify revert to which migration


### Seed operations
Executes scripts in `seed` directory

Create first seed  
`npx sequelize-cli seed:generate --name demo-user`

Run seeds  
`npx sequelize-cli db:seed:all`

Undo seeds  
`npx sequelize-cli db:seed:undo[:all]`

## Storage
Sequelize stores executed migration script names to identify new migration scripts. If a script is identified as executed in one environment, it won't be executed again.

There are 3 types of storage, user can change storage configurations in `config/config.js` generated at initialization.

 - `sequelize` Stores migrations and seeds names in a table (**SequelizeMeta**), default option
 - `json` Stores migrations and seeds names in a JSON file
 - `none` Doesn't store any migrations and seeds names

## Others
`Model.bulkCreate(records, {updateOnDuplicate: ['attr_name1'], ignoreDuplicates: false})`
`updateOnDuplicate`  Fields to update if primary key duplicates, only supported by MySQL  
`ignoreDuplicates`  Ignore duplicate values for primary keys, not supported by MySQL or Postgres < 9.5

